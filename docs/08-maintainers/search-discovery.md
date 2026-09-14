# 搜索发现与 GEO 维护

官网地址：<https://bao-776.github.io/personal-knowledge-system-skills/>

## 证据分层

维护时分别记录以下状态，不将前一层描述成后一层：

1. **可访问**：公开 URL 返回正常页面。
2. **已抓取**：搜索引擎访问过页面。
3. **已收录**：可在搜索索引中找到页面。
4. **产生展示或点击**：Search Console 或 Bing Webmaster Tools 有对应数据。
5. **被生成式回答引用**：具体问题、回答、日期和引用链接均有截图或记录。

## 首次发布

1. 确认 GitHub Pages 部署成功，并回读中文页、英文页、`robots.txt` 和 `sitemap.xml`。
2. 在 Google Search Console 添加 URL-prefix 资源并完成所有权验证。
3. 提交 `https://bao-776.github.io/personal-knowledge-system-skills/sitemap.xml`，分别检查中文首页和英文页。
4. 在 Bing Webmaster Tools 导入 Google Search Console 站点，或独立完成验证，再提交同一个 sitemap。
5. IndexNow 只用于通知 Bing 等支持方新增、更新或删除的 URL。它不能保证抓取、收录或排名；小型静态站首版可先使用 sitemap 和手动 URL 提交。

账号验证和站长平台提交属于外部账号操作，应由仓库所有者完成或明确授权后执行。验证码或验证文件不得写入通用模板。

## 内容维护

- 页面标题、主标题、简介和结构化数据对项目的描述保持一致。
- 版本变化时同步更新页面正文、JSON-LD、分享图信息、`VERSION` 和 changelog。
- 新增可索引页面时更新 sitemap，并为每页提供唯一标题、简介和 canonical。
- 功能描述必须能够回到仓库文档、模板或测试证据；不使用虚构评价、效果数字或排名承诺。
- FAQ 回答真实问题，服务读者理解；不为获取富媒体结果制造重复问题。
- 英文内容按英文用户的搜索和阅读习惯独立撰写，不逐句复制中文。

## 监测节奏

发布后第 1、2、4 周记录一次基线，此后仅在版本发布或内容有实质变化时检查：

| 日期 | 页面 | 可访问 | 已抓取 | 已收录 | 展示/点击 | 生成式引用 | 证据位置 |
|---|---|---|---|---|---|---|---|
| 待填写 | 中文首页 | 待检查 | 待检查 | 待检查 | 待检查 | 待检查 | 待填写 |
| 待填写 | 英文页 | 待检查 | 待检查 | 待检查 | 待检查 | 待检查 | 待填写 |

建议观察的查询包括项目名称，以及“Codex 个人知识库”“AI 知识库 Skill”“Obsidian 原子笔记”“Codex skills for knowledge management”“evidence-based personal knowledge system”等真实用途表达。查询是否带来展示，以站长平台数据为准。

## 参考

- [Google：AI features and your website](https://developers.google.com/search/docs/appearance/ai-features)
- [Google：Influencing title links](https://developers.google.com/search/docs/appearance/title-link)
- [Google：SEO Starter Guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide)
- [Bing：IndexNow](https://www.bing.com/indexnow/getstarted)
- [Bing：Sitemaps](https://www.bing.com/webmasters/help/Sitemaps-3b5cf6ed)
- [GitHub：About GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/about-github-pages)
