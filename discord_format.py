class DiscordFormat:
    @staticmethod
    def bold(str) -> str:
        return f"**{str}**"

    @staticmethod
    def spoiler(str) -> str:
        return f"||{str}||"
