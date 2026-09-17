// 向每个页面注入自定义样式表（配合 source/css/custom.css）
hexo.extend.injector.register('head', () => '<link rel="stylesheet" href="/css/custom.css">');
