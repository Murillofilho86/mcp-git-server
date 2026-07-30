from mcp.server.fastmcp import FastMCP
import subprocess

mcp = FastMCP("mcp-git-server")

# TODO: `git_status` — estado do repo apontado (~25 min, inclui setup inicial e boilerplate)
@mcp.tool()
def git_status(repo_path: str) -> str:
    """Show working tree status of a git repository.
    
    Use this when you need to see what files are modified, staged,
    or untracked in a repository before making decisions.
    
    Args:
        repo_path: Absolute path to the git repository
    """
    result = subprocess.run(
        ["git", "-C", repo_path, "status", "--short", "--branch"],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        return f"Error: {result.stderr.strip()}"
    return result.stdout.strip() or "Working tree clean"

# TODO: `git_log` — commits recentes, parametrizado por quantidade (~20 min)
@mcp.tool()
def git_log(repo_path: str, limit: int = 10) -> str:
    """Show recent commit history in short format.
    
    Args:
        repo_path: Absolute path to the git repository
        limit: Number of commits to show (default 10, max recommended 50)
    """
 
    result = subprocess.run(
        ["git", "-C", repo_path, "log", f"-{limit}", "--online", "--decorate"],
        capture_output=True,
        text=True,
        check=False,    
    )
    if result.returncode != 0:
        return f"Error: {result.stderr.strip()}"
    return result.stdout.strip()

# TODO: `git_diff` — diff parametrizado por ref ou range (~25 min)


if __name__ == "__main__":
    mcp.run()