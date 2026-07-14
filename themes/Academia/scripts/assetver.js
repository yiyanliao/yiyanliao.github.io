/**
 * Cache-busting: stamp one build-time version onto local CSS/JS URLs so browsers
 * fetch the new files immediately after a deploy instead of serving stale copies.
 * Computed once per `hexo generate`, so every page in a build shares the same value.
 */
hexo.on('generateBefore', function () {
    hexo.theme.config.asset_version = Date.now();
});
