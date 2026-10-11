# Bases

Use native Bases for repeated fields, filters, sorting, and views. Define one clear source folder or property filter. Each view should answer a user question. Keep data in notes; the Base is a view, not the source of truth. Provide a Markdown fallback. The learning-resources example expects resource notes with `type: learning-resource`, `learning_status: queued` or `learning`, and `next_action`; learning notes and growth candidates are different types and must not be relabeled to force a match. For a resource card, use these fields plus title/source, purpose, and created/updated dates as needed. Test the example with a matching note before reporting it works.


Minimal matching resource frontmatter (adapt local conventions; a resource is not a learning note):

```yaml
type: learning-resource
learning_status: queued
next_action: Read the introductory chapter
sources:
  - https://example.org/resource
```

Add a purpose in the body. `queued` does not make the resource an active priority. Verify the Current view includes queued/learning resources and excludes learning-note/growth-candidate types; describe GUI results only when observed.
