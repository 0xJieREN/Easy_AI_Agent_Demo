# Easy AI Agent Demo

[![Python](https://img.shields.io/badge/Python-3.13+-blue.svg)](https://www.python.org/downloads/)
[![Pydantic-AI](https://img.shields.io/badge/Pydantic--AI-0.4.7+-green.svg)](https://github.com/baidu/pydantic-ai)

A simple yet powerful AI agent system based on the DeepSeek large language model, capable of performing file operations and intelligent conversations.

<!--  -->
## Features

- 🤖 Intelligent Conversations with DeepSeek LLM
- 📁 File System Operations
  - Read file contents
  - List directory files
  - Rename files
  - Write files (with safety checks)
- 🔒 Security Protection
  - File operations restricted to specified directory
  - Prevention of accidental file overwrites
- 💬 Continuous Dialogue Support
  - Maintain conversation history
  - Markdown formatted output

## Requirements

- Python 3.13+
- pydantic-ai 0.4.7+
- python-dotenv
- rich

## Quick Start

1. Clone the repository and install dependencies:

```bash
git clone 
cd Easy-AI-Agent-Demo
pip install -r requirements.txt
```

2. Set up environment variables:
   Create a `.env` file and add your DeepSeek API key:

```
OPENAI_API_KEY=your_api_key_here
```

3. Run the program:

```bash
python main.py
```

## Usage

After starting the program, you can interact with the AI agent through the command line. The AI agent can:

- Read files: View the contents of specified files
- List files: Display all files in a directory
- Rename files: Safely rename files
- Write files: Create new files or update existing ones (with explicit confirmation for overwrites)

All file operations are restricted to the `./test` directory for security.

## Project Structure

```
AI_agent/
├── main.py          # 主程序入口
├── tool.py          # 文件操作工具函数
├── pyproject.toml   # 项目配置文件
└── test/            # 文件操作的测试目录
```

## Future Improvements

1. Feature Enhancements

   - [ ] Add file deletion functionality
   - [ ] Add directory creation functionality
   - [ ] Support file permission management
   - [ ] Add file content search functionality

2. Security Improvements

   - [ ] Add file operation logging
   - [ ] Implement file operation rollback mechanism
   - [ ] Add file type checking

3. User Experience

   - [ ] Add command-line argument support
   - [ ] Implement interactive configuration interface
   - [ ] Add progress display functionality
   - [ ] Improve error messages

4. Performance Optimization

   - [ ] Implement asynchronous file operations
   - [ ] Add file caching mechanism
   - [ ] Optimize large file handling capabilities

5. Integration Enhancements
   - [ ] Add support for more AI models
   - [ ] Implement plugin system
   - [ ] Add API interface

## Contributing

Contributions are welcome! If you want to contribute:

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

[MIT License](LICENSE)
