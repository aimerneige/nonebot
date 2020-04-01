# CQ_lessons
基于nonebot框架的简单的课表提醒小助手

使用时请配合nontebot框架使用

如果要自定义课程提醒，请先看config文件中的注释提醒
nonebot文档链接如下：
https://nonebot.netlify.com/

导入方式：
在main文件中添加如下代码：
```python
if __name__=='__main__':
    nonebot.init(config)#初始化nonebot包
    nonebot.load_plugins(
        path.join(path.dirname(__file__),'awesome','plugins'),
        'awesome.plugins'
    )
    nonebot.run()
```
后续自动导csv课表功能还在开发中（咕咕咕）