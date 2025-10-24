"""Minimal application code for gfg_store."""

def greet(name: str = "World") -> str:
    """Return a greeting for the given name."""
    return f"Hello, {name}!"

def main() -> None:
    """CLI entry point."""
    print(greet())

if __name__ == "__main__":
    main()