# CDN for Local Businesses: What Edge Hosting Actually Does, in Plain English
## 本地企业的 CDN 入门：边缘托管到底做了什么，用大白话讲清

> **TL;DR:** A CDN keeps copies of a website's public files on servers in many cities and serves each visitor from a nearby copy. Pages load from the closest copy, the main server handles fewer repeat requests, and a traffic spike in one city stays a local event. A local business gets the most from a CDN by caching public pages and images aggressively, keeping checkout and account pages uncached, and checking real load times from the cities its customers live in.

## Start with the delivery problem

A business website usually lives on one server in one city. A visitor across the country asks that server for the homepage, the photos, the style files, and the scripts, one request after another. Each request travels the full distance, and the page assembles only after the slowest pieces arrive. Distance adds delay to every file, and a busy hour multiplies the effect because one machine answers everyone at once. Edge hosting attacks that delivery problem directly: copies of the site already sit near the visitor, so most files travel a short hop.

## What the edge copy holds

The edge copy holds files that stay the same for every visitor. Typical contents:

- Page HTML for public pages such as services, pricing, and contact
- Photos, logos, and other images
- Style sheets and script files
- Downloadable documents such as menus, forms, and brochures

Account pages, checkout screens, and anything personalized stay off the shared copy. Those requests pass through to the main server, which answers them fresh for each signed-in visitor. The split matters for safety as much as for speed: a shared copy should only ever hold material that is already public.

## How a single visit flows

A visitor in Chicago opens the site of a cleaning company based in Los Angeles. The browser asks for the homepage. A nearby edge server checks its copy, finds the current version, and sends it straight back. The photos and style files come from the same nearby copy. The main server in Los Angeles hears about none of those requests. The visitor then opens the booking form and submits it. That request travels to the main server, because a booking needs live data and a fresh answer. One visit, two paths: public files from the edge, live actions from the origin.

## Where the gains show up, and where they stop

Repeat visits gain the most, because browsers and edge servers both reuse stored files. First visits gain when the visitor lives far from the main server. Photo-heavy pages gain more than plain text pages, because images carry most of the bytes on a typical service page. The gains stop at live work. A CDN cannot speed up a slow booking database, a payment step that waits on a bank, or a page the main server builds slowly on every request. Teams sometimes blame the CDN for a sluggish checkout when the delay sits in the origin application. Measure each path separately: time the public pages from a distant city, then time the booking flow, and fix whichever number is actually slow.

## A setup sequence that works for a small site

1. List the public pages and file types the edge may cache, and write down the exceptions (account, checkout, admin) on the same page.
2. Set a cache lifetime per file type: long for images and documents that rarely change, shorter for page HTML that staff edit often.
3. Add a version step to the publishing routine, so a replaced photo or script gets a new file name and visitors receive the new file at once.
4. Turn on HTTPS at the edge and confirm the certificate renews automatically.
5. Purge the cache after a major site update, then reload the key pages from two different cities to confirm the new version is live everywhere.

## Stale copies are the main operational risk

A cached copy can outlive the page it copied. The classic failure is small and embarrassing: the business changes its opening hours, the main site shows the new hours, and visitors in one region keep seeing the old hours from a stale copy. The fixes are procedural. Page HTML gets a short cache lifetime. Every content update ends with a purge of the changed pages. Staff check the live site through the CDN after publishing, from an outside connection. The editing preview alone does not count as that check. Our earlier note on [static-first websites](2026-11-16-static-first-websites.md) pairs well with this setup, because static pages cache cleanly and rarely surprise anyone. Dynamic pages need the shorter lifetimes and the stricter purge habit described above.

## Decide with measurements from your own cities

Generic speed scores hide the number that matters most: how long the page takes for your customers, where they actually live. Before adopting a CDN, record load times for the homepage and the heaviest service page from the two or three cities that send the most visitors. Repeat the same measurements a week after setup, at a similar hour. Compare like with like, and keep the raw numbers in the operations log. A business with mostly local customers and a nearby server may find the gap small, and that is a valid finding too. The decision rests on measured distance. KINGAI publishes its sites on edge infrastructure as part of the intelligent website work behind [kingai.work](https://kingai.work), and the same measurement routine decides which pages cache aggressively and which stay live.

## Quick reference

| Page or file | Cache at the edge? | Reason |
|---|---|---|
| Service and pricing pages | Yes, short lifetime | Public, edited from time to time |
| Photos and logos | Yes, long lifetime | Large files, rarely change |
| Menus and downloadable forms | Yes, long lifetime | Public documents, versioned by file name |
| Booking and checkout | No | Live data, personal to each visitor |
| Account and admin pages | No | Private by definition |

---

*Technical support by kingai.work*

---

# 本地企业的 CDN 入门：边缘托管到底做了什么，用大白话讲清

> **摘要**：CDN 把网站的公开文件复制到许多城市的服务器上，访客从离自己近的那一份取文件。页面从最近的副本加载，主服务器少答大量重复请求，某个城市突然涌入的流量也只是一个局部事件。本地企业要用好 CDN，关键是把公开页面和图片放心缓存、结账与账户页面不进缓存，并从客户真正所在的城市实测加载时间。

## 先看清交付问题出在哪

企业网站通常住在一座城市的一台服务器上。外地访客打开网站时，首页、照片、样式文件和脚本要一个接一个地向这台服务器索取。每个请求都要走完全程，页面要等最慢的那几个文件到齐才拼得出来。距离给每个文件都加上延迟，繁忙时段更明显，因为所有人同时在问同一台机器。边缘托管直接对着这个交付问题下手：网站的副本提前放在访客附近，大多数文件只需走很短一段路。

## 边缘副本里放什么

边缘副本存放对每位访客都一样的文件，常见内容包括：

- 服务、价格、联系等公开页面的 HTML
- 照片、标志和其他图片
- 样式表与脚本文件
- 可下载的文档，如菜单、表单和宣传册

账户页面、结账界面和一切带个人信息的页面不进共享副本。这类请求直接回到主服务器，由它为每位登录访客现答。这条分界对安全和速度同样重要：共享副本里只应存放本来就公开的内容。

## 一次访问实际怎么走

一位芝加哥访客打开洛杉矶一家保洁公司的网站。浏览器请求首页，附近的边缘服务器查到自己的副本是最新版，直接发回。照片和样式文件也来自同一份近处副本。洛杉矶的主服务器对这些请求一无所知。访客接着打开预约表单并提交，这次请求走回主服务器，因为预约需要实时数据和一次现算的答复。一次访问，两条路径：公开文件走边缘，实时动作走源站。

## 收益出现在哪里，又在哪里止步

重复访问收益最大，因为浏览器和边缘服务器都会复用已存文件。访客离主服务器越远，首次访问的收益越明显。图片多的页面比纯文字页面收益大，因为一个典型服务页里，图片占了大部分字节。收益止步于实时环节。CDN 加速不了慢吞吞的预约数据库，也加速不了等银行回应的支付步骤，更加速不了主服务器每次请求都要现拼半天的页面。有的团队结账慢就怪 CDN，其实延迟出在源站应用上。两条路径要分开测：从外地城市测公开页面的加载时间，再测预约流程的时间，哪条慢修哪条。

## 小站可照做的配置顺序

1. 列出边缘可以缓存的公开页面和文件类型，并把例外（账户、结账、后台）写在同一页上。
2. 按文件类型设缓存时长：很少改的图片和文档设长一些，员工常改的页面 HTML 设短一些。
3. 发布流程里加一步版本管理：换掉的照片或脚本用新文件名上线，访客立刻拿到新文件。
4. 在边缘开启 HTTPS，并确认证书自动续期。
5. 网站大更新后清一次缓存，再从两座不同的城市重新打开关键页面，确认各处拿到的都是新版本。

## 过期副本是主要的运营风险

缓存副本可能比它复制的页面活得久。最典型的翻车很小却难堪：企业改了营业时间，主站已经显示新时间，某个地区的访客却一直从过期副本里看到旧时间。修法全在流程上。页面 HTML 的缓存时长设短。每次内容更新以清掉被改页面的缓存收尾。员工发布后要通过 CDN、从外部连接打开线上站点核对。编辑预览不算数，以线上打开的结果为准。我们此前关于 [静态优先网站](2026-11-16-static-first-websites.md) 的文章与这套配置正好搭配，因为静态页面缓存干净、很少出意外。动态页面则需要上面写的更短缓存时长和更严格的清理习惯。

## 用自己城市的数据做决定

通用测速分数会盖住最要紧的数字：页面在你的客户实际所在的城市打开要多久。上 CDN 之前，先从带来最多访客的两三座城市，记录首页和最重的那个服务页的加载时间。上线一周后，在相近时段重复同样的测量。两次测同一组页面，把原始数字记进运营日志。客户大多在本地、服务器也在附近的企业，可能会发现差距很小，这同样是一个成立的结论。决定应建立在实测的距离上。KINGAI 在 [kingai.work](https://kingai.work) 背后的智慧网站工作中把站点发布在边缘基础设施上，同一套实测流程决定哪些页面放心缓存、哪些保持实时。

## 速查表

| 页面或文件 | 是否在边缘缓存 | 理由 |
|---|---|---|
| 服务与价格页面 | 是，短时长 | 公开内容，会不时修改 |
| 照片与标志 | 是，长时长 | 文件大，很少改动 |
| 菜单与可下载表单 | 是，长时长 | 公开文档，用文件名做版本 |
| 预约与结账 | 否 | 实时数据，每位访客各不相同 |
| 账户与后台页面 | 否 | 本质上就是私密内容 |

---

*由 kingai.work 提供技术支持*
