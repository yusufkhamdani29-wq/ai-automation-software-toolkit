// ==UserScript==
// @name         Copy Page as Markdown
// @namespace    https://example.com/ai-automation-toolkit
// @version      1.0
// @description  Press Alt+M on any page to copy its title and URL as a Markdown link, plus any selected text as a quote.
// @author       AI Automation & Software Toolkit
// @match        *://*/*
// @grant        none
// ==/UserScript==

(function () {
  'use strict';

  function toMarkdown() {
    var title = document.title.trim();
    var url = location.href;
    var selection = window.getSelection ? window.getSelection().toString().trim() : '';
    var out = '[' + title + '](' + url + ')';
    if (selection) {
      var quoted = selection.split('\n').map(function (line) {
        return '> ' + line;
      }).join('\n');
      out += '\n\n' + quoted;
    }
    return out;
  }

  function copyText(text) {
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).catch(function () {
        fallbackCopy(text);
      });
    } else {
      fallbackCopy(text);
    }
  }

  function fallbackCopy(text) {
    var ta = document.createElement('textarea');
    ta.value = text;
    ta.style.position = 'fixed';
    ta.style.opacity = '0';
    document.body.appendChild(ta);
    ta.select();
    try { document.execCommand('copy'); } catch (e) { /* clipboard unavailable */ }
    document.body.removeChild(ta);
  }

  document.addEventListener('keydown', function (e) {
    if (e.altKey && (e.key === 'm' || e.key === 'M')) {
      e.preventDefault();
      copyText(toMarkdown());
    }
  });
})();
