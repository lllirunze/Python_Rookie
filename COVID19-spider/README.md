### 任务总况  

- 疫情当下，思考如何快速获取实时的中国风险地区名单助力疫情防控

### 网站解析与代码实现

- 通过对蚌埠市提供《全国疫情中高风险地区名单》的信息多日追踪后发现，其url固定（https://www.bengbu.gov.cn/public/22601/49996408.html），可以作为定时爬取的途径
- 采用 requests 代码完成数据爬取
- 分析其网页源代码，可以发现，所需要信息以文本形式在源代码中展示
- 分析源代码，《全国中高风险地区名单》标题以 标签"gk_title"出现，具体名单在p标签内，因此考虑使用BeautifuSoup 对数据进行筛选提取

### 数据输出与动态保存

- 考虑名单是实时更新的，因此采用time.strftime随计算机时间重命名保存文件
