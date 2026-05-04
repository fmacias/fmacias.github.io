(function () {
  var preferenceKey = "site_lang";
  var sourceKey = "site_lang_source";
  var path = window.location.pathname || "/";
  var normalized = path.replace(/\/+$/, "");

  function getLanguageFromPath(pathname) {
    if (pathname === "/de" || pathname.indexOf("/de/") === 0) {
      return "de";
    }

    if (pathname === "/es" || pathname.indexOf("/es/") === 0) {
      return "es";
    }

    return "en";
  }

  function setPreference(language, source) {
    localStorage.setItem(preferenceKey, language);
    localStorage.setItem(sourceKey, source);
  }

  function hasManualPreference() {
    return localStorage.getItem(sourceKey) === "manual";
  }

  function updateLanguageSwitcherLinks() {
    var hash = window.location.hash || "";
    var links = document.querySelectorAll(".md-select__link[hreflang]");

    links.forEach(function (link) {
      var href = link.getAttribute("href");
      if (!href) {
        return;
      }

      var url = new URL(href, window.location.origin);
      url.hash = hash ? hash.substring(1) : "";
      link.setAttribute("href", url.pathname + url.search + url.hash);
    });
  }

  document.addEventListener(
    "click",
    function (event) {
      if (!event.target || !event.target.closest) {
        return;
      }

      var link = event.target.closest(".md-select__link[hreflang]");
      if (!link) {
        return;
      }

      var language = (link.getAttribute("hreflang") || "").toLowerCase();
      if (!language) {
        return;
      }

      setPreference(language, "manual");
    },
    true
  );

  document.addEventListener("DOMContentLoaded", updateLanguageSwitcherLinks);
  window.addEventListener("hashchange", updateLanguageSwitcherLinks);
  updateLanguageSwitcherLinks();

  if (normalized === "") {
    return;
  }

  if (!hasManualPreference()) {
    setPreference(getLanguageFromPath(normalized), "auto");
  }
})();
