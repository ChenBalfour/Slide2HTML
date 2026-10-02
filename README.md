# Slide2HTML

把课程 PPT、PDF、讲义和作业要求，转成**精美、可追溯、可离线打开的双语 HTML 学习页**。

## 安装到 Codex：只下载一个 ZIP

**[点击下载 slide2html-plugin.zip](https://github.com/ChenBalfour/Slide2HTML/raw/refs/heads/main/dist/slide2html-plugin.zip)**

1. 点击上面的链接，保存 `slide2html-plugin.zip`。**不需要解压、不需要逐个下载文件，也不需要自己打包。**
2. 在 Codex 的插件页面打开「添加插件」（部分界面显示「新建插件」），选择这个 ZIP，完成添加并确认插件已启用。
3. 新建一个聊天，上传课程 PPT、PDF 或讲义，发送下面这句话：

   > 使用 slide2html 技能，把这些课件转成精美的离线 HTML 学习页，默认中文，支持英文切换。

4. 下载生成的 `slide2html.html`，双击用浏览器打开。生成的学习页可以离线阅读。

安装不需要 Python、命令行或额外 MCP 服务。课件读取、OCR 和生成后的浏览器验证能力取决于你使用的环境。

**已经安装旧版？** 重新导入新版 ZIP；如果界面提示重名且没有更新入口，先移除旧插件再添加新版，然后新建聊天。修改 GitHub 文件不会自动刷新之前上传的安装包。

**下载时不要选错：** GitHub 绿色「Code → Download ZIP」下载的是整个项目源码，带有外层仓库文件夹，不能原封不动地当作插件包导入。上面的专用下载链接提供已打包的安装文件。

## 装好后能做什么

一个可读文件即可开始：讲义生成知识指南，作业生成要求清单，多份课程材料生成整合学习中心。

也可指定：“只整理这次作业的提交要求”“做成深色研究笔记风格”“默认英文”“显示中英对照”“沿用现有页面样式”。用户明确要求优先于 skill 默认值。

## 看看生成页的设计方向

[打开设计示例的源码/下载入口](skills/slide2html/examples/slide2html.html)，下载后双击用浏览器打开。暖白与深墨色、编辑式排版和课程概念图形，包含中英切换、双语搜索与来源详情。**内容是合成材料，不是真实课程，也不是所有页面的固定模板。**

高级感来自字体层级、留白、布局、内容节奏与主题视觉，不依赖 CDN 字体、庞大组件库或装饰性数据。每次生成应适配课程内容和用户审美。

## 其他安装方式（可选）

<details>
<summary>不通过插件入口，手动安装到本地 Skills 目录</summary>

下载并解压整个项目后，复制 **`skills/slide2html/` 这个完整文件夹**，放到所用工具支持的 Skills 目录，保留文件夹名 `slide2html`。不要复制整个仓库，也不要把内部文件打散。具体 Skills 路径和启用方式按该工具说明操作。

完整文件夹包含技能说明、参考规则、可选检查脚本和设计示例。只想安装最小版本时，至少保留以下四个文件及其目录关系；检查脚本和示例不会随最小版本安装：

```text
slide2html/
├── SKILL.md
└── references/
    ├── analysis-framework.md
    ├── html-specification.md
    └── quality-control.md
```

这个方式安装的是裸 Skill，不适用于 Codex 的「添加插件」ZIP 入口。

</details>

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
dist/slide2html-plugin.zip         # 用户直接下载的安装包
scripts/build_plugin.py           # 维护者重新生成安装包
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

普通用户只需下载开头的安装包。维护者修改文件后，在仓库根目录运行下面的命令重新打包，并将新的 `dist/slide2html-plugin.zip` 一起提交：

```sh
python scripts/build_plugin.py
```

脚本只打包插件清单、README 和 `skills/` 中的运行资源，排除 Git 元数据、缓存、测试和旧安装包；ZIP 内没有外层仓库文件夹。

插件详情页的项目链接配置在根目录 `plugin.json` 的 `extensions.com.openai.interface.websiteURL`，同时在 `.codex-plugin/plugin.json` 的 `interface.websiteURL` 保留相同值。`homepage`、`repository` 也指向本项目，但不能代替展示字段；已有安装需要导入新版 ZIP 才能使用新元数据。参见 [OpenAI 插件清单文档](https://developers.openai.com/plugins/deploy/submission)。

验证命令：

```sh
python skills/slide2html/scripts/validate_html.py skills/slide2html/examples/slide2html.html
python -m unittest discover -s tests -v
```

静态检查不运行 JavaScript，也不保证外观或事实正确。新增或大改页面还应在浏览器中检查桌面、手机、语言切换、搜索和离线行为。用[评估场景](tests/evaluation-scenarios.md)做实际生成的对照测试；工具不足时如实记录验证范围。
