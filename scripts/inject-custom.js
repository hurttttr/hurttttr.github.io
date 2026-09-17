// 向每个页面注入自定义样式表（配合 source/css/custom.css）
hexo.extend.injector.register('head', () => '<link rel="stylesheet" href="/css/custom.css">');

// 侧栏「最近发布」整卡可点：主题模板里标题/分类是 span（href 属性无效），点击无反应。
// 事件委托挂在 document 上，pjax 切页后依然有效。
hexo.extend.injector.register('bottom', () => `<script>
document.addEventListener('click', function (e) {
  var item = e.target.closest('.aside-list-item');
  if (!item || e.target.closest('a')) return;
  var link = item.querySelector('a.thumbnail[href]') || item.querySelector('a[href]');
  if (link) window.location.href = link.href;
});
</script>`);
