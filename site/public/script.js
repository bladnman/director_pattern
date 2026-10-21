for (const button of document.querySelectorAll('[data-copy-from]')) {
  button.addEventListener('click', async () => {
    const source = document.getElementById(button.dataset.copyFrom);
    const status = button.parentElement.querySelector('[role="status"]');
    const text = source.textContent;
    try {
      if (!navigator.clipboard?.writeText) throw new Error('Clipboard unavailable');
      await navigator.clipboard.writeText(text);
      status.textContent = 'Copied. Paste into your project agent.';
    } catch {
      const range = document.createRange();
      range.selectNodeContents(source);
      const selection = window.getSelection();
      selection.removeAllRanges();
      selection.addRange(range);
      status.textContent = 'Text selected. Copy it, then paste into your project agent.';
    }
  });
}
