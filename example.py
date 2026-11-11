from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain_core.prompts import ChatPromptTemplate
import os

# Qwen3.8-Max qwen3.8-max
# 模型介绍 qwen3.8 深度思考 视觉理解 文本生成
# 2.4万亿参数MoE旗舰，编程与办公能力全面跃升，可自主编程十数天交付完整项目。胜任法律、金融、设计等数百种专业任务，一次对话端到端交付生产级成果。原生视觉理解贯穿规划、执行与验证全流程，支持超长文档与长视频的深度语义解析。长程任务中自主规划与闭环迭代，持续进化。

# Qwen3.8-Max-0902 qwen3.8-max-0902
# 模型介绍 qwen3.8 文本生成 视觉理解 深度思考
# Qwen3.8-Max-0902（别名qwen3.8-max-2026-09-02）是qwen3.8-max的快照版本。编码深度再突破，可驾驭更复杂的工程级项目与长程自主开发；协作智能体能力显著增强，在多工具调度与端到端交付中表现更从容；视觉理解全面精进，图表推理、文档解析与多模态感知更敏锐准确。延续 100 万上下文、思考模式与完整工具生态，在更高智能水平上持续进化。

llm = ChatOpenAI(
    # model="qwen3-max",
    # model="qwen3.8-max",
    model="qwen3.8-max-0902",
    openai_api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("user", "Give me the introduction information of this city: {city}.")
])

chain = LLMChain(llm=llm, prompt=prompt)

city = "San Francisco"
resp = chain.run({"city": city})
print(resp)

### 演示样例案例 ###

### 运行样例
### python example.py