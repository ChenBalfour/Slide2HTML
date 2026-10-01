# Slide2HTML

把课程 PPT、PDF、讲义和作业要求，转成**精美、可追溯、可离线打开的双语 HTML 学习页**。

面向支持文件读取、文件生成与 Skills 的 AI 工具。一个可读文件即可开始：讲义生成知识指南，作业生成要求清单，多份课程材料生成整合学习中心。格式读取、OCR 与浏览器验证能力取决于所用工具。

## 看看设计方向

[打开设计示例的源码/下载入口](skills/slide2html/examples/slide2html.html)，下载后双击用浏览器打开。暖白与深墨色、编辑式排版和课程概念图形，包含中英切换、双语搜索与来源详情。**内容是合成材料，不是真实课程，也不是所有页面的固定模板。**

高级感来自字体层级、留白、布局、内容节奏与主题视觉，不依赖 CDN 字体、庞大组件库或装饰性数据。每次生成应适配课程内容和用户审美。

## 使用

### 从 Codex「添加插件」导入

本仓库根目录是插件目录，Skill 的实际入口为 [`skills/slide2html/SKILL.md`](skills/slide2html/SKILL.md)。根目录包含 `plugin.json` 与 `.codex-plugin/plugin.json`，插件使用环境已有的工具，无需额外 MCP 服务。

下载并解压本仓库后，在仓库根目录使用 PowerShell 打包：

```powershell
Compress-Archive -Path .codex-plugin,plugin.json,skills,README.md -DestinationPath ..\slide2html-plugin.zip -Force
```

在 Codex 的「添加插件」窗口中选择生成的 `slide2html-plugin.zip`。插件清单与 `skills/` 必须位于 ZIP 根目录，不能再套一层仓库文件夹。原来的 `slide2html.zip` 是裸 Skill 包，不能直接用于插件上传入口。实际导入是否成功须由客户端结果确认。

### 安装到本地 Skills 目录

1. 将本仓库的 `skills/slide2html/` 文件夹复制到所用工具支持的 Skills 目录，保留文件夹名 `slide2html`；安装路径和启用方式请按该工具说明操作。
2. 真正必需的是这 4 个文件，目录结构要保留：
```text
slide2html/
├── SKILL.md
└── references/
    ├── analysis-framework.md
    ├── html-specification.md
    └── quality-control.md
```
3. 上传可读取的课程材料，或提供本地文件路径。
4. 请求：“把这些课件转成精美的离线 HTML 学习页，默认中文，支持英文切换。”
5. 下载生成的 `slide2html.html`，用浏览器直接打开。

也可指定：“只整理这次作业的提交要求”“做成深色研究笔记风格”“默认英文”“显示中英对照”“沿用现有页面样式”。用户明确要求优先于 skill 默认值。

## 默认能力

- **来源可追溯**：关键事实与知识点保留真实来源和页码/幻灯片定位。
- **材料驱动**：整合重复概念，呈现有证据的关联；不强制生成无关模块。
- **双语阅读**：主要内容保留完整中英版本，默认显示用户语言，可即时切换；需要时提供对照视图。
- **考核与冲突**：按需提取评分、提交要求、政策和日期；保留不确定性与矛盾，不编造缺失信息。
- **离线单文件**：CSS、JS 和展示资产内嵌，无构建步骤；外部资源链接的目标仍需网络。
- **精美与可用**：主题化视觉、响应式布局、可访问控件；长内容按需提供搜索、筛选或学习进度。

浏览器可能限制本地文件的持久化存储。若生成页含进度功能，应在存储不可用时继续工作并提示仅本次会话有效。

## 文件结构

```text
.codex-plugin/plugin.json         # Codex 插件清单与展示信息
plugin.json                       # 插件清单
skills/slide2html/
  SKILL.md                        # 精简入口、证据约束与按需路由
  references/
    analysis-framework.md         # 复杂材料、考核、版本与证据
    html-specification.md         # 高端视觉、双语与离线实现
    quality-control.md            # 事实、文件与浏览器验收
  scripts/
    validate_html.py              # 零第三方依赖的静态检查
  examples/
    source-notes.md               # 合成示例材料
    slide2html.html               # 可直接打开的设计样例
tests/
  test_validate_html.py           # 检查脚本的回归测试
  evaluation-scenarios.md         # 维护者使用的行为评估场景
```

## 为什么精简

新版将强制 20 步流程、重复角色定义、固定全课程结构，改成按任务选择深度的工作流。参考文件按需读取，保留会改变决策的规则。视觉从固定 SaaS 配色改为课程相关的高端排版标准。

这符合 OpenAI 当前关于[缩短描述、按需披露和减少过度流程约束](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra)的建议。**指令更短不等于质量必然更高，也不代表已经测得总 token 节省**：课件提取、双语正文、代码生成和验证仍有开销。应使用相同模型、材料与工具比较结果、token 和耗时。

完整双语会增加正文生成量；默认只显示一种语言改善阅读体验，不会自动减少生成两种语言的成本。skill 不绑定特定模型版本。

## 维护与验证

```sh
python skills/slide2html/scripts/validate_html.py skills/slide2html/examples/slide2html.html
python -m unittest discover -s tests -v
```

静态检查不运行 JavaScript，也不保证外观或事实正确。新增或大改页面还应在浏览器中检查桌面、手机、语言切换、搜索和离线行为。用[评估场景](tests/evaluation-scenarios.md)做实际生成的对照测试；工具不足时如实记录验证范围。
