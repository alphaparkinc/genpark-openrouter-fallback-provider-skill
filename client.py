class OpenRouterFallbackProviderClient:
    def get_fallback(self, primary_model: str, error_code: int) -> dict:
        fallback = "openai/gpt-4o-mini" if "claude" in primary_model else "meta-llama/llama-3-8b-instruct"
        return {"fallback_model": fallback}