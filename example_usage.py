from client import OpenRouterFallbackProviderClient
client = OpenRouterFallbackProviderClient()
print(client.get_fallback("anthropic/claude-3-sonnet", 429))