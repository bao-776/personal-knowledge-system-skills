"use strict";
(() => {
  const buttons = [...document.querySelectorAll("[data-step]")];
  const panels = [...document.querySelectorAll(".demo-stage")];
  function selectStep(index) {
    buttons.forEach((button, i) => button.setAttribute("aria-pressed", String(i === index)));
    panels.forEach((panel, i) => { panel.hidden = i !== index; });
  }
  buttons.forEach((button, index) => button.addEventListener("click", () => selectStep(index)));
  if (buttons.length) selectStep(0);
  const profile = document.getElementById("profile");
  const command = document.getElementById("install-command");
  const status = document.getElementById("copy-status");
  const isEnglish = document.documentElement.lang === "en";
  profile?.addEventListener("change", () => {
    const base = `python -X utf8 scripts/install_codex_skills.py <codex-skills-directory> --profile ${profile.value}`;
    command.textContent = `${base} --dry-run\n${base}\n${base} --verify`;
    status.textContent = "";
  });
  document.getElementById("copy-command")?.addEventListener("click", async () => {
    try {
      await navigator.clipboard.writeText(command.textContent);
      status.textContent = isEnglish ? "Copied. Replace the target path before running." : "已复制，运行前请替换目标路径。";
    } catch {
      status.textContent = isEnglish ? "Clipboard unavailable. Select and copy the command above." : "剪贴板不可用，请选中上方命令复制。";
    }
  });
})();
