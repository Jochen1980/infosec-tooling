exports.footer = {
  height: '0.8cm',
  contents: function (pageNum, numPages) {
    return "<div style='float:left;font-size: 0.5em;font-family: monospace;color:#555;'>Stand: " + new Date().toLocaleDateString() + "&nbsp;&nbsp;&nbsp;[intern (K2)]</div><div style='float:right;font-size: 0.6em;font-family: monospace;color:#555;text-align:right;'>Seite " + pageNum + " von " + numPages + "</div>";
  }
};