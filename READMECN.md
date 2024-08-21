# 全自动陶瓷信生成Agent

## 概述

**陶瓷信生成器** 是非常方便的RAG框架下的基于 Flask 的网络应用程序，帮助用户生成个性化的研究兴趣信件。用户可以上传他们的简历，应用程序会根据相关的学术信息和研究兴趣，使用 OpenAI GPT 模型生成量身定制的信件。该工具旨在帮助学生申请研究机会、实习或助理职位，通过创建高质量、针对性强的信件提高竞争力。

## 功能

- **简历上传**：用户可以通过界面直接上传简历。
- **个性化信件**：应用程序根据用户简历、教授的研究兴趣和其他输入生成个性化的研究信件。
- **多种 GPT 模型支持**：支持 `gpt-3.5-turbo` 和 `gpt-4` 模型生成信件。
- **Google Scholar 集成**：使用 SerpAPI 的 Google Scholar 引擎获取教授的相关学术信息。
- **用户友好界面**：简单直观的前端设计，使信件生成过程更加容易。

## 项目结构

```
research_letter_generator/
│
├── app.py                            # 主应用入口
├── config.py                         # 配置文件，存储 API 密钥和设置
├── controllers/
│   └── research_letter_controller.py # 处理请求路由和业务逻辑
├── services/
│   ├── letter_generator.py           # 核心服务，用于生成研究信件
│   ├── serp_api_service.py           # 服务，用于与 SerpAPI 交互获取学术信息
│   └── openai_service.py             # 服务，用于与 OpenAI API 交互
├── templates/
│   ├── research_interest_advanced.html # 信件提交表单的 HTML 模板
│   └── showCL.html                    # 显示生成信件的 HTML 模板
└── static/
    └── css/
        └── styles.css                # 网站应用的自定义样式
```

## 快速开始

### 先决条件

在开始之前，请确保您满足以下要求：

- **Python 3.7+**
- **Flask**: 通过运行 `pip install Flask` 安装 Flask。
- **OpenAI API 密钥**：需要从 [OpenAI](https://beta.openai.com/signup/) 获取 API 密钥。
- **SerpAPI 密钥**：需要从 [SerpAPI](https://serpapi.com/) 获取 API 密钥。

### 安装

1. **克隆仓库：**

   ```bash
   git clone https://github.com/yourusername/research-letter-generator.git
   cd research-letter-generator
   ```

2. **安装依赖项：**

   安装所需的 Python 包：

   ```bash
   pip install -r requirements.txt
   ```

3. **设置配置文件：**

   在项目根目录下创建 `.env` 文件，并添加您的 API 密钥：

   ```
   SECRET_KEY=your_flask_secret_key
   API_KEY_SERP=your_serp_api_key
   OPENAI_API_KEY=your_openai_api_key
   ```

4. **运行应用程序：**

   启动 Flask 服务器：

   ```bash
   python app.py
   ```

   应用程序将在 `http://127.0.0.1:5000/` 上运行。

### 使用方法

1. **访问应用程序：**

   打开浏览器，进入 `http://127.0.0.1:5000/research_interest_advanced`。

2. **上传简历：**

   填写您的姓名、教授的姓名、大学名称以及任何特殊偏好。上传您的简历，格式可以为 `.txt`、`.pdf` 或 `.docx`。

3. **生成信件：**

   点击“提交”按钮生成两份研究兴趣信。

4. **查看信件：**

   生成的信件将在下一个页面展示。您可以复制并根据需要使用这些信件。

### 自定义

- **模型选择**：您可以在表单中选择使用 `gpt-3.5-turbo` 或 `gpt-4` 来生成信件。
- **样式**：通过编辑 `static/css/styles.css` 文件，您可以自定义应用程序的外观。
- **模板**：修改 `templates` 目录中的 HTML 模板来调整用户界面。

### 贡献

如果您想为本项目做出贡献，请 Fork 该仓库并提交 Pull Request。我们欢迎所有改进和建议。

### 许可证

本项目采用 MIT 许可证。详见 `LICENSE` 文件。

### 联系方式

如果您有任何问题或反馈，请随时联系：

- **姓名**：在学习的皮卡丘@小红书

---

### 其他说明：

- **错误处理**：请确保所有异常，特别是涉及外部 API 调用的异常，都能被妥善处理。
- **安全性**：在部署到生产环境时，请记得对您的应用程序进行安全设置。

这个 README 以中文提供了清晰的指导，使其他人能够轻松理解该项目的目的和功能。
