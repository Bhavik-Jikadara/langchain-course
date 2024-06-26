# [Chat Models](https://python.langchain.com/v0.1/docs/integrations/chat/)

Chat Models are a core component of LangChain.

A chat model is a language model that uses chat messages as inputs and returns chat messages as outputs (as opposed to using plain text).

LangChain has integrations with many model providers (OpenAI, Cohere, Hugging Face, etc.) and exposes a standard interface to interact with all of these models.

LangChain allows you to use models in sync, async, batching and streaming modes and provides other features (e.g., caching) and more.

## Features

All ChatModels implement the Runnable interface, which comes with default implementations of all methods, ie. ainvoke, batch, abatch, stream, astream. This gives all ChatModels basic support for async, streaming and batch, which by default is implemented as below:

- **Async Support**: By default, async operations use asyncio's thread pool executor to run synchronous methods in the background, enabling other async tasks to continue concurrently.

- **Streaming Support**: Streaming provides an iterator (or AsyncIterator for async operations) that yields the final result from the ChatModel provider, allowing flexible integration with applications expecting iterable outputs.

- **Batch Support**: Batch processing executes ChatModel operations in parallel:
  - Sync batch processing uses a thread pool executor for concurrency.
  - Async batch processing utilizes asyncio.gather to handle multiple async tasks concurrently, adjustable via parameters like max_concurrency.

Each ChatModel integration can optionally provide native implementations to truly enable async or streaming. The table shows, for each integration, which features have been implemented with native support.

<table>
        <thead>
            <tr>
                <th align="left">Model</th>
                <th align="center">Invoke</th>
                <th align="center">Async invoke</th>
                <th align="center">Stream</th>
                <th align="center">Async stream</th>
                <th align="center"><a href="/v0.1/docs/modules/model_io/chat/function_calling/">Tool calling</a></th>
                <th align="center"><a href="/v0.1/docs/modules/model_io/chat/structured_output/">Structured output</a>
                </th>
                <th align="center">Python Package</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td align="left">AzureChatOpenAI</td>
                <td align="center">✅</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">✅</td>
                <td align="center">✅</td>
                <td align="center">langchain-openai</td>
            </tr>
            <tr>
                <td align="left">BedrockChat</td>
                <td align="center">✅</td>
                <td align="center">❌</td>
                <td align="center">✅</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">langchain-community</td>
            </tr>
            <tr>
                <td align="left">ChatAnthropic</td>
                <td align="center">✅</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">✅</td>
                <td align="center">✅</td>
                <td align="center">langchain-anthropic</td>
            </tr>
            <tr>
                <td align="left">ChatAnyscale</td>
                <td align="center">✅</td>
                <td align="center">✅</td>
                <td align="center">✅</td>
                <td align="center">✅</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">langchain-community</td>
            </tr>
            <tr>
                <td align="left">ChatBaichuan</td>
                <td align="center">✅</td>
                <td align="center">❌</td>
                <td align="center">✅</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">langchain-community</td>
            </tr>
            <tr>
                <td align="left">ChatCohere</td>
                <td align="center">✅</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">✅</td>
                <td align="center">✅</td>
                <td align="center">langchain-cohere</td>
            </tr>
            <tr>
                <td align="left">ChatCoze</td>
                <td align="center">✅</td>
                <td align="center">❌</td>
                <td align="center">✅</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">langchain-community</td>
            </tr>
            <tr>
                <td align="left">ChatDatabricks</td>
                <td align="center">✅</td>
                <td align="center">❌</td>
                <td align="center">✅</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">langchain-community</td>
            </tr>
            <tr>
                <td align="left">ChatDeepInfra</td>
                <td align="center">✅</td>
                <td align="center">✅</td>
                <td align="center">✅</td>
                <td align="center">✅</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">langchain-community</td>
            </tr>
            <tr>
                <td align="left">ChatEverlyAI</td>
                <td align="center">✅</td>
                <td align="center">✅</td>
                <td align="center">✅</td>
                <td align="center">✅</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">langchain-community</td>
            </tr>
            <tr>
                <td align="left">ChatFireworks</td>
                <td align="center">✅</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">✅</td>
                <td align="center">✅</td>
                <td align="center">langchain-fireworks</td>
            </tr>
            <tr>
                <td align="left">ChatFriendli</td>
                <td align="center">✅</td>
                <td align="center">✅</td>
                <td align="center">✅</td>
                <td align="center">✅</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">langchain-community</td>
            </tr>
            <tr>
                <td align="left">ChatGooglePalm</td>
                <td align="center">✅</td>
                <td align="center">✅</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">langchain-community</td>
            </tr>
            <tr>
                <td align="left">ChatGroq</td>
                <td align="center">✅</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">✅</td>
                <td align="center">✅</td>
                <td align="center">langchain-groq</td>
            </tr>
            <tr>
                <td align="left">ChatHuggingFace</td>
                <td align="center">✅</td>
                <td align="center">✅</td>
                <td align="center">✅</td>
                <td align="center">✅</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">langchain-community</td>
            </tr>
            <tr>
                <td align="left">ChatHunyuan</td>
                <td align="center">✅</td>
                <td align="center">❌</td>
                <td align="center">✅</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">langchain-community</td>
            </tr>
            <tr>
                <td align="left">ChatJavelinAIGateway</td>
                <td align="center">✅</td>
                <td align="center">✅</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">langchain-community</td>
            </tr>
            <tr>
                <td align="left">ChatKinetica</td>
                <td align="center">✅</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">langchain-community</td>
            </tr>
            <tr>
                <td align="left">ChatKonko</td>
                <td align="center">✅</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">langchain-community</td>
            </tr>
            <tr>
                <td align="left">ChatLiteLLM</td>
                <td align="center">✅</td>
                <td align="center">✅</td>
                <td align="center">✅</td>
                <td align="center">✅</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">langchain-community</td>
            </tr>
            <tr>
                <td align="left">ChatLiteLLMRouter</td>
                <td align="center">✅</td>
                <td align="center">✅</td>
                <td align="center">✅</td>
                <td align="center">✅</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">langchain-community</td>
            </tr>
            <tr>
                <td align="left">ChatMLX</td>
                <td align="center">✅</td>
                <td align="center">✅</td>
                <td align="center">✅</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">langchain-community</td>
            </tr>
            <tr>
                <td align="left">ChatMLflowAIGateway</td>
                <td align="center">✅</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">langchain-community</td>
            </tr>
            <tr>
                <td align="left">ChatMaritalk</td>
                <td align="center">✅</td>
                <td align="center">✅</td>
                <td align="center">✅</td>
                <td align="center">✅</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">langchain-community</td>
            </tr>
            <tr>
                <td align="left">ChatMistralAI</td>
                <td align="center">✅</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">✅</td>
                <td align="center">✅</td>
                <td align="center">langchain-mistralai</td>
            </tr>
            <tr>
                <td align="left">ChatMlflow</td>
                <td align="center">✅</td>
                <td align="center">❌</td>
                <td align="center">✅</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">langchain-community</td>
            </tr>
            <tr>
                <td align="left">ChatOctoAI</td>
                <td align="center">✅</td>
                <td align="center">✅</td>
                <td align="center">✅</td>
                <td align="center">✅</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">langchain-community</td>
            </tr>
            <tr>
                <td align="left">ChatOllama</td>
                <td align="center">✅</td>
                <td align="center">✅</td>
                <td align="center">✅</td>
                <td align="center">✅</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">langchain-community</td>
            </tr>
            <tr>
                <td align="left">ChatOpenAI</td>
                <td align="center">✅</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">✅</td>
                <td align="center">✅</td>
                <td align="center">langchain-openai</td>
            </tr>
            <tr>
                <td align="left">ChatPerplexity</td>
                <td align="center">✅</td>
                <td align="center">❌</td>
                <td align="center">✅</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">langchain-community</td>
            </tr>
            <tr>
                <td align="left">ChatPremAI</td>
                <td align="center">✅</td>
                <td align="center">❌</td>
                <td align="center">✅</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">langchain-community</td>
            </tr>
            <tr>
                <td align="left">ChatSparkLLM</td>
                <td align="center">✅</td>
                <td align="center">❌</td>
                <td align="center">✅</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">langchain-community</td>
            </tr>
            <tr>
                <td align="left">ChatTongyi</td>
                <td align="center">✅</td>
                <td align="center">✅</td>
                <td align="center">✅</td>
                <td align="center">✅</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">langchain-community</td>
            </tr>
            <tr>
                <td align="left">ChatVertexAI</td>
                <td align="center">✅</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">✅</td>
                <td align="center">✅</td>
                <td align="center">langchain-google-vertexai</td>
            </tr>
            <tr>
                <td align="left">ChatYandexGPT</td>
                <td align="center">✅</td>
                <td align="center">✅</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">langchain-community</td>
            </tr>
            <tr>
                <td align="left">ChatYuan2</td>
                <td align="center">✅</td>
                <td align="center">✅</td>
                <td align="center">✅</td>
                <td align="center">✅</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">langchain-community</td>
            </tr>
            <tr>
                <td align="left">ChatZhipuAI</td>
                <td align="center">✅</td>
                <td align="center">✅</td>
                <td align="center">✅</td>
                <td align="center">✅</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">langchain-community</td>
            </tr>
            <tr>
                <td align="left">ErnieBotChat</td>
                <td align="center">✅</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">langchain-community</td>
            </tr>
            <tr>
                <td align="left">GPTRouter</td>
                <td align="center">✅</td>
                <td align="center">✅</td>
                <td align="center">✅</td>
                <td align="center">✅</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">langchain-community</td>
            </tr>
            <tr>
                <td align="left">GigaChat</td>
                <td align="center">✅</td>
                <td align="center">✅</td>
                <td align="center">✅</td>
                <td align="center">✅</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">langchain-community</td>
            </tr>
            <tr>
                <td align="left">JinaChat</td>
                <td align="center">✅</td>
                <td align="center">✅</td>
                <td align="center">✅</td>
                <td align="center">✅</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">langchain-community</td>
            </tr>
            <tr>
                <td align="left">LlamaEdgeChatService</td>
                <td align="center">✅</td>
                <td align="center">❌</td>
                <td align="center">✅</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">langchain-community</td>
            </tr>
            <tr>
                <td align="left">MiniMaxChat</td>
                <td align="center">✅</td>
                <td align="center">✅</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">langchain-community</td>
            </tr>
            <tr>
                <td align="left">PaiEasChatEndpoint</td>
                <td align="center">✅</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">✅</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">langchain-community</td>
            </tr>
            <tr>
                <td align="left">PromptLayerChatOpenAI</td>
                <td align="center">✅</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">langchain-community</td>
            </tr>
            <tr>
                <td align="left">QianfanChatEndpoint</td>
                <td align="center">✅</td>
                <td align="center">✅</td>
                <td align="center">✅</td>
                <td align="center">✅</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">langchain-community</td>
            </tr>
            <tr>
                <td align="left">SolarChat</td>
                <td align="center">✅</td>
                <td align="center">✅</td>
                <td align="center">✅</td>
                <td align="center">✅</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">langchain-community</td>
            </tr>
            <tr>
                <td align="left">VolcEngineMaasChat</td>
                <td align="center">✅</td>
                <td align="center">❌</td>
                <td align="center">✅</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">❌</td>
                <td align="center">langchain-community</td>
            </tr>
        </tbody>
    </table>
