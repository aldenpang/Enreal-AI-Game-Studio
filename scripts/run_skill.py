#!/usr/bin/env python3
import argparse
import os
from pathlib import Path

try:
    import yaml
    from openai import OpenAI
except Exception as e:
    raise SystemExit("Missing deps. Run: pip install pyyaml openai")


def load_provider(cfg_path: Path, provider_name: str | None):
    cfg = yaml.safe_load(cfg_path.read_text(encoding="utf-8"))
    provider_name = provider_name or cfg.get("default_provider")
    if provider_name not in cfg["providers"]:
        raise SystemExit(f"Provider not found: {provider_name}")
    p = cfg["providers"][provider_name]
    api_key = os.getenv(p.get("api_key_env", "OPENAI_API_KEY"), "dummy")
    return provider_name, p["base_url"], p["model"], api_key


def main():
    ap = argparse.ArgumentParser(description="Run a studio skill with any OpenAI-compatible model")
    ap.add_argument("skill", help="skill name, e.g. start, design-system")
    ap.add_argument("prompt", help="user request for this skill")
    ap.add_argument("--provider", default=None, help="provider key from config/providers.example.yaml")
    ap.add_argument("--config", default="config/providers.example.yaml")
    ap.add_argument("--repo", default=".")
    args = ap.parse_args()

    repo = Path(args.repo).resolve()
    skill_file = repo / ".studio" / "skills" / args.skill / "SKILL.md"
    if not skill_file.exists():
        raise SystemExit(f"Skill not found: {skill_file}")

    provider_name, base_url, model, api_key = load_provider(repo / args.config, args.provider)
    system = (
        "You are a game-development specialist agent runner. "
        "Follow the skill instructions exactly, keep outputs actionable, "
        "and preserve the Ask→Options→Decision→Draft flow."
    )
    skill_text = skill_file.read_text(encoding="utf-8")

    client = OpenAI(base_url=base_url, api_key=api_key)
    completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system},
            {"role": "system", "content": f"SKILL SPEC:\n\n{skill_text}"},
            {"role": "user", "content": args.prompt},
        ],
        temperature=0.4,
    )

    print(f"# Provider: {provider_name}\n# Model: {model}\n")
    print(completion.choices[0].message.content or "")


if __name__ == "__main__":
    main()
