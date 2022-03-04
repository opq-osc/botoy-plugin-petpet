# botoy-plugin-petpet

**注意，请点击 [fork](https://github.com/opq-osc/botoy-plugin-petpet/network/members) 查看原创地址**

因为 opq 的消息格式很不规范，所以很多地方的修改都是本着能跑就行的心态，望知悉 😂

使用 `botoy plugin install https://github.com/opq-osc/botoy-plugin-petpet.git petpet` 安装，
安装后记得安装依赖 `pip install -r requirements.txt`

### 使用

下面的指令为 pp 或者 /

发送“头像表情包”显示下图的列表：

<div align="left">
  <img src="https://s2.loli.net/2022/02/23/lxgQ6tnoXNZECWj.jpg" width="400" />
</div>

~~每个表情包首次使用时会下载对应的图片和字体，可以手动下载 `resources` 下的 `images` 和 `fonts` 文件夹，放置于机器人运行目录下的 `data/petpet/` 文件夹中~~
图片及字体资源调整到了.resources 下，会随 git clone 自动下载

#### 触发方式

- 指令 + @user，如： /爬 @小 Q
- 指令 + qq 号，如：/爬 123456
- 指令 + 自己，如：/爬 自己
- 指令 + 图片，如：/爬 [图片]

前三种触发方式会使用目标 qq 的头像作为图片

如果`/`触发与其他插件冲突，可以使用`pp/`作为前缀

#### 支持的指令

- 摸

<div align="left">
  <img src="https://s2.loli.net/2022/02/23/oNGVO4iuCk73g8S.gif" width="200" />
</div>

- 亲

<div align="left">
  <img src="https://s2.loli.net/2022/02/23/RuoiqP8plJBgw9K.gif" width="200" />
</div>

- 贴/蹭

<div align="left">
  <img src="https://s2.loli.net/2022/02/23/QDCE5YZIfroavub.gif" width="200" />
</div>

- 顶/玩

<div align="left">
  <img src="https://s2.loli.net/2022/02/23/YwxA7fFgWyshuZX.gif" width="200" />
</div>

- 拍

<div align="left">
  <img src="https://s2.loli.net/2022/02/23/5mv6pFJMNtzHhcl.gif" width="200" />
</div>

- 撕

<div align="left">
  <img src="https://s2.loli.net/2022/02/23/DNIix6W1OmqknhU.jpg" width="200" />
</div>

- 丢

<div align="left">
  <img src="https://s2.loli.net/2022/02/23/LlDrSGYdpcqEINu.jpg" width="200" />
</div>

- 爬

<div align="left">
  <img src="https://s2.loli.net/2022/02/23/hfmAToDuF2actC1.jpg" width="200" />
</div>

- 精神支柱

<div align="left">
  <img src="https://s2.loli.net/2022/02/23/WwjNmiz4JXbuE1B.jpg" width="200" />
</div>

- 一直

<div align="left">
  <img src="https://s2.loli.net/2022/02/23/dAf9Z3kMDwYcRWv.gif" width="200" />
</div>

- 加载中

<div align="left">
  <img src="https://s2.loli.net/2022/02/23/751Oudrah6gBsWe.gif" width="200" />
</div>

- 转

<div align="left">
  <img src="https://s2.loli.net/2022/02/23/HoZaCcDIRgs784Y.gif" width="200" />
</div>

- 小天使

<div align="left">
  <img src="https://s2.loli.net/2022/02/23/ZgD1WSMRxLIymCq.jpg" width="200" />
</div>

- 不要靠近

<div align="left">
  <img src="https://s2.loli.net/2022/02/23/BTdkAzvhRDLOa3U.jpg" width="200" />
</div>

- 一样

<div align="left">
  <img src="https://s2.loli.net/2022/02/23/SwAXoOgfdjP4ecE.jpg" width="200" />
</div>

- 滚

<div align="left">
  <img src="https://s2.loli.net/2022/02/23/atzZsSE53UDIlOe.gif" width="200" />
</div>

- 玩游戏

<div align="left">
  <img src="https://s2.loli.net/2022/02/23/Xx34I7nT8HjtfKi.png" width="200" />
</div>

- 膜

<div align="left">
  <img src="https://s2.loli.net/2022/02/23/nPgBJwV5qDb1s9l.gif" width="200" />
</div>

- 吃

<div align="left">
  <img src="https://s2.loli.net/2022/02/23/ba8cCtIWEvX9sS1.gif" width="200" />
</div>

- 啃

<div align="left">
  <img src="https://s2.loli.net/2022/02/23/k82n76U4KoNwsr3.gif" width="200" />
</div>

- 出警

<div align="left">
  <img src="https://s2.loli.net/2022/02/23/3OIxnSZymAfudw2.jpg" width="200" />
</div>

- 问问

<div align="left">
  <img src="https://s2.loli.net/2022/02/23/GUyax1BF6q5Hvin.jpg" width="200" />
</div>
