#!/usr/bin/env python
# coding=utf-8
import asyncio
from aiohttp import TCPConnector, ClientSession

import pyecharts.options as opts
from pyecharts.charts import Sankey

"""
Gallery 使用 pyecharts 1.0.0
参考地址: https://echarts.baidu.com/examples/editor.html?c=sankey-energy

目前无法实现的功能:

1、label 和图的层次有点问题
"""


async def get_json_data(url: str) -> dict:
    async with ClientSession(connector=TCPConnector(ssl=False)) as session:
        async with session.get(url=url) as response:
            return await response.json()


# 获取官方的数据
data = asyncio.run(
    get_json_data(url="https://echarts.baidu.com/examples/data/asset/data/energy.json")
)

(
    Sankey(init_opts=opts.InitOpts(width="1600px", height="800px"))
    .add(
        series_name="",
        nodes=data["nodes"],
        links=data["links"],
        itemstyle_opts=opts.ItemStyleOpts(border_width=1, border_color="#aaa"),
        linestyle_opt=opts.LineStyleOpts(color="source", curve=0.5, opacity=0.5),
        tooltip_opts=opts.TooltipOpts(trigger_on="mousemove"),
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="Sankey Diagram"))
    .render("sankey_diagram.html")
)
