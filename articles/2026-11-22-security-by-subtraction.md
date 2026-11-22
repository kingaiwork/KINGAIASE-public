# Security by Subtraction: Removing Unused Logins, Plugins, and Stale Pages
## 减法式安全：清理闲置登录、插件与过期页面

> **TL;DR** — Every login, plugin, and published page is a surface someone has to maintain, patch, and watch. A small team improves security by shrinking that surface on a regular schedule: inventory what exists, remove accounts and extensions with no current owner or purpose, retire pages that no longer serve visitors, and record each removal so the next review starts from a clean list. The work is procedural; it fits into a monthly hour, and it reduces the number of forgotten entry points an attacker can find first.

## Start with an inventory you can finish

A complete inventory is the foundation of subtraction, because you can only remove what you can see. List every place a person or a system can sign in: the website admin, hosting, domain registrar, analytics, email marketing, and any connected third-party tools. Next to each account, write the owner, the purpose, and the date it was last used. Do the same for plugins and integrations, noting what each one does and which page or workflow depends on it. Finish with a page list from your sitemap or content system, marking each page as current, outdated, or orphaned with no inbound links. A spreadsheet is enough for this step. Accuracy matters more than tooling.

## Remove logins that have lost their owner

Dormant accounts are the highest-value removals, because they often keep working long after the person behind them has moved on. Review accounts belonging to former staff, former contractors, and shared mailboxes that nobody monitors. Where a role still needs access, reissue it to a named person with the least privilege the role requires, and turn on multi-factor authentication during the same session. Delete test accounts, demo accounts, and duplicate accounts for the same person. Keep one documented break-glass admin path, store its credentials in a password manager, and test it after the cleanup so the team retains a recovery route.

## Treat every plugin as a standing permission

An installed plugin holds ongoing access to your site, so each one deserves a current reason to stay. For every plugin or extension, ask three questions. Who owns it today? What breaks if it is disabled for a day? When was it last updated by its maintainer? Plugins with no owner, no clear dependency, or a long gap since the last update are removal candidates. Disable one at a time, check the pages and forms that might depend on it, and then delete it fully rather than leaving it deactivated in the codebase. Deactivated code can still sit on the server, and a tidy removal closes that gap. Replace overlapping tools with one maintained option where the overlap is real, and record the choice in the inventory.

## Retire stale pages with a redirect, not a disappearance

Old pages carry risk when they run outdated scripts, collect form data nobody reads, or publish offers and policies the business has changed. Review each outdated page and choose one of three outcomes. Update it when the topic still matters to visitors. Merge it into a current page when a stronger version covers the same ground. Retire it when the topic has ended, and point its address to the closest relevant page with a redirect. Check retired addresses after the change, and review form endpoints on old pages with extra care, because a forgotten form can keep collecting personal data with no owner reading the submissions. Our earlier note on [backup restore drills](2026-11-19-backup-restore-drill.md) covers the companion habit: before a cleanup day, take a backup and confirm it restores, so a mistaken removal stays reversible.

## Use a table to decide, then act the same day

Subtraction stalls when every item becomes a debate, so decide with fixed criteria and act in the same session. The table below gives a working rule set for a small team.

| Item | Keep when | Remove or retire when |
|---|---|---|
| User account | A named owner uses it for current work | The owner has left, or no one used it in the review period |
| Plugin or extension | A named owner relies on it and updates arrive regularly | No owner, no dependency, or updates have stopped |
| Published page | It serves a current offer, policy, or question | The offer has ended, or a current page covers the topic better |
| Form endpoint | A named owner reads and acts on submissions | Submissions go unread, or the form duplicates another intake |
| Third-party integration | A live workflow depends on it weekly | The workflow ended, or the tool was a trial that never launched |

## Make subtraction a monthly habit with an owner

A single cleanup helps for a while, and a recurring review keeps the surface small as the team adds tools and pages through the year. Put a one-hour review on the calendar each month, assign one owner, and work from the inventory rather than from memory. Each session should end with four updates to that inventory: accounts removed, plugins removed, pages retired or merged, and items flagged for the next session. Note who approved each removal, because a short decision record prevents repeat debates and helps a new team member understand why something is gone. KINGAI applies this subtraction routine in the ongoing operations work behind [kingai.work](https://kingai.work), treating removal as a standard part of keeping client systems maintainable. Teams that prefer to run it themselves can start with the inventory alone; the first list usually reveals the first removals within the hour.

## A closing check before you finish a cleanup session

Close each session by verifying that the smaller surface still works end to end. Sign in with each remaining admin account, submit each live form once, and open the pages that depended on removed plugins. Confirm the redirects from retired pages land on relevant destinations, and confirm the break-glass account still works. Record the date, the owner, and the counts in the inventory. That closing check turns subtraction from a tidying exercise into a security control with evidence, and it gives the next monthly review a reliable starting point.

---

*Technical support by kingai.work*

---

# 减法式安全：清理闲置登录、插件与过期页面

> **摘要**：每一个登录入口、插件和已发布页面，都是一处需要有人维护、更新和盯守的面。小团队按固定节奏缩小这个面，安全状况就会改善：先盘点现有资产，再清掉没有现任负责人或用途的账号与扩展，下线不再服务访客的页面，并把每次移除记录在案，让下一次复查从一份干净的清单开始。这套做法全是流程动作，一个月留出一小时就能做完，也能减少被攻击者先发现的闲置入口。

## 先做一份能做完的盘点

完整的盘点是做减法的基础，因为看不见的东西无从清理。先列出所有能登录的地方：网站后台、主机、域名注册商、统计分析、邮件营销，以及接入的各类第三方工具。每个账号旁边写清负责人、用途和最近一次使用日期。插件和集成也照此办理，注明各自的功能，以及哪个页面或流程依赖它。最后从站点地图或内容系统导出页面清单，把每页标为现行、过期，或没有入站链接的孤页。这一步用电子表格就够了，准确比工具重要。

## 清理失去负责人的登录账号

闲置账号是最值得先清的一类，因为人已经离开，账号往往还在继续生效。逐个复查前员工、前外包人员留下的账号，以及无人查看的共享邮箱账号。岗位确实还需要权限的，重新发给具名个人，只给该岗位所需的最小权限，并在同一次操作中开启多重验证。测试账号、演示账号和同一人的重复账号一并删除。保留一条有记录的应急管理员通道，凭据存入密码管理器，清理完成后实际登录测试一次，确认团队仍有恢复路径。

## 把每个插件都当作一份持续授权

装上的插件对站点握有持续访问权，所以每一个都应有当下留存的理由。对每个插件或扩展问三个问题：今天谁负责它？停用一天会坏什么？维护者最近一次更新是什么时候？没有负责人、依赖关系说不清，或长期没有更新的，先列为清理候选。逐个停用，检查可能依赖它的页面与表单，确认无碍后彻底删除，不要只停用后留在代码里。停用的代码仍可能留在服务器上，彻底删除才算关上这处缺口。功能重叠的工具，在重叠属实处合并为一个有人维护的选项，并把决定记入盘点表。

## 过期页面用重定向下线，不让它凭空消失

旧页面若仍在运行过期脚本、收集无人查看的表单数据，或挂着商家已经变更的优惠与政策，就会带来风险。逐页复查过期页面，在三个结果中选一个：话题对访客仍有价值的，更新它；已有更完整页面覆盖同一话题的，合并过去；话题已经结束的，下线该页，并把它的地址用重定向指向最相关的一个现行页面。改完后逐个打开已下线的地址核对落点，旧页面上的表单入口要格外留意，因为无人负责的表单可能持续收集个人信息却无人处理。我们此前关于 [备份恢复演练](2026-11-19-backup-restore-drill.md)的文章谈过与之配套的习惯：清理日之前先做一份备份并确认能恢复，误删时才有退路。

## 用一张表做决定，并在当天执行

每件资产都争论一遍，减法就会停滞，所以要用固定标准做决定，并在同一次工作中执行。下表给出一套小团队可直接采用的判断规则。

| 对象 | 保留条件 | 移除或下线条件 |
|---|---|---|
| 用户账号 | 具名负责人正用于现行工作 | 负责人已离开，或复查周期内无人使用 |
| 插件或扩展 | 具名负责人依赖它，且更新正常 | 无负责人、无依赖，或已停止更新 |
| 已发布页面 | 服务于现行优惠、政策或访客问题 | 优惠已结束，或现行页面覆盖得更好 |
| 表单入口 | 具名负责人会查看并处理提交 | 提交无人查看，或与另一入口重复 |
| 第三方集成 | 现行流程每周都在用它 | 流程已结束，或只是从未上线的试用 |

## 把减法变成有负责人的月度习惯

清理一次只能管一阵，把复查做成例行动作，才能在团队全年不断新增工具与页面的同时，把攻击面一直保持在小规模。每月在日历上留一小时，指定一名负责人，照盘点表工作，不凭记忆。每轮结束时在盘点表上更新四项：删了哪些账号、删了哪些插件、下线或合并了哪些页面、哪些留待下轮处理。每项移除记下批准人，一份简短的决定记录能避免反复争论，也方便新成员理解某样东西为什么不在了。KINGAI 在 [kingai.work](https://kingai.work) 背后的持续运营工作中执行这套减法例行，把移除当作保持客户系统可维护的标准环节。想自己执行的团队可以只从盘点起步，第一份清单通常在一小时内就能指出第一批可清项。

## 清理收尾前的一次核查

每轮结束时，验证缩小后的系统仍然端到端可用。用每个保留的管理员账号各登录一次，每个现行表单各提交一次，打开曾依赖已删插件的页面逐一查看。确认下线页面的重定向落点相关且正确，确认应急账号仍可登录。把日期、负责人和各项计数记入盘点表。这一步收尾核查，能把减法从一次整理变成一项有据可查的安全控制，也给下个月的复查留下一个可靠的起点。

---

*由 kingai.work 提供技术支持*
