# Role-Based Access Control for Small Business Systems: Permissions Before Features
## 小企业系统的角色权限管理：先定权限，再加功能

> **TL;DR:** Role-based access control gives each person in a small business system exactly the permissions their job requires, grouped into named roles such as owner, manager, staff, and finance. The practical route is to define roles from real tasks, write them into a one-page permission matrix, and review membership whenever someone joins, changes jobs, or leaves. Systems set up this way make onboarding faster, audits calmer, and mistakes easier to trace.

## The admin-for-everyone habit

Small systems usually start with one shared admin account, created on the day the software went in. As the team grows, that account gets copied, the password travels, and soon five people can change prices, export the customer list, and delete records. Day-to-day work feels smooth, right up to the first incident: a deleted invoice nobody can explain, a discount applied by an unknown hand, a former contractor whose login still works. The root cause in these stories is rarely malice. The system simply never recorded who was allowed to do what, so it cannot show who did it. Role-based access control, usually shortened to RBAC, fixes that gap by attaching permissions to roles and roles to people.

## Define roles from jobs, not from people

A role is a bundle of permissions that matches a job. The reliable way to define roles is to list the tasks each job performs in the system, then grant the permissions those tasks require. A typical small business lands on four or five roles:

| Role | Typical permissions | Deliberately out of scope |
|---|---|---|
| Owner | Everything, including billing, role management, and data export | Nothing in the system, so this role stays rare |
| Manager | Approve orders and refunds, edit schedules, view reports | Billing settings and role management |
| Staff | Create and edit daily records, handle assigned customers | Refunds, exports, and deletion of shared records |
| Finance | Invoices, payments, reconciliation, financial reports | Service settings and customer messaging |
| External help | One named module, time-boxed for a project | Everything outside that module |

Two design rules keep the table honest. First, each role starts empty and earns permissions task by task, which keeps grants deliberate. Second, a person holds the smallest set of roles that covers their work. A bookkeeper who also answers support tickets holds Finance plus a limited support role, and each role stays narrow enough to explain in one sentence.

## Identity answers "who"; permissions answer "what"

RBAC works alongside sign-in rather than replacing it. A unified account tells the system who is at the keyboard; roles decide what that person may open, edit, approve, or delete. Our earlier article on [one account for every product](2026-11-20-unified-sign-in-one-account.md) covers the identity side of that pairing. The permission side deserves equal care, because a verified login with excessive rights still exposes the business. When both halves are in place, a staff member signs in once, sees the tools their job needs, and meets a clear stop at the boundary of someone else's job.

## A one-page permission matrix is the working document

The matrix is a plain grid: rows for actions, columns for roles, a mark where an action is allowed. Building it takes one focused session with the people who run the business. A practical sequence:

1. List the actions that carry risk: payments, refunds, price changes, data export, record deletion, user management, and settings changes.
2. Walk each action across the roles and mark who may perform it, who may approve it, and who should stay out entirely.
3. Mark the actions that require a second person, such as a refund above a set amount or a change to bank details.
4. Save the matrix where the team can find it, with a date and an owner.

The matrix then drives configuration. Each system setting gets compared against the grid, and any mismatch is either a setting to fix or a matrix line to debate openly. Either way the decision lands on paper, which is where permission decisions belong.

## Joiners, movers, and leavers keep roles current

Roles drift when people change and the system stays still. A short routine tied to staff changes keeps the roster accurate:

- **Joiner:** create the account on day one, assign roles from the matrix, and record who approved the assignment.
- **Mover:** when someone changes jobs, remove the old roles in the same step that adds the new ones, so privileges from a previous post retire on schedule.
- **Leaver:** disable the account on the final working day, transfer ownership of their records to a named colleague, and check for shared credentials to rotate.

Shared accounts undermine all of this, because actions under a shared login belong to nobody. Where a tool forces a shared login, for example a legacy supplier portal, the team records who holds the credential, stores it in the company password manager, and rotates it whenever a holder leaves. The exception stays visible and managed instead of quiet and forgotten.

## Review on a calendar, and read the logs you already have

A quarterly review keeps the design close to reality. The owner or a manager prints the role roster, checks each name against current jobs, and removes access that no longer matches. The same session samples the activity log for sensitive actions: exports, deletions, permission changes. Most small systems already record these events; the review simply gives someone the job of reading them. Findings feed back into the matrix, and the matrix carries a new date.

Permission work also pays off during ordinary growth. A new feature lands more safely when the team first asks which roles may use it, because the question forces a decision about who owns the new capability. KINGAI applies this permissions-first approach in the business systems work behind [kingai.work](https://kingai.work), where role design is part of the initial setup rather than a later cleanup. A small business can adopt the same order of work with modest effort: one matrix, four or five roles, and a calendar reminder each quarter.

---

*Technical support by kingai.work*

---

# 小企业系统的角色权限管理：先定权限，再加功能

> **摘要**：基于角色的访问控制，是给小企业系统里的每个人分配与其岗位相匹配的权限，并把权限归入所有者、经理、员工、财务等具名角色。落地做法是按真实工作任务定义角色，把结果写成一页权限矩阵，并在人员入职、转岗、离职时同步复核成员资格。这样建起来的系统，入职开通更快，事后核查更从容，出错时也更容易追溯到具体环节。

## 人人都是管理员的惯性

小系统起步时通常只有一个共用的管理员账户，还是软件装上那天建的。团队一大，这个账户被复制、密码被转手，很快就有五个人能改价格、导出客户名单、删除记录。日常用起来似乎顺手，直到第一次出事：一张被删掉又说不清来历的发票、一笔不知谁批的折扣、一个早已离职的外包人员还能用的登录。复盘这类事情，根源很少是恶意。系统从头到尾没有记录过谁有权做什么，自然也就说不清是谁做的。基于角色的访问控制（英文缩写 RBAC）补的正是这个缺口：权限挂在角色上，角色再分配给具体的人。

## 按岗位定义角色，不按人头

角色是与一个岗位相匹配的一组权限。可靠的定义方法是先列出每个岗位在这个系统里实际要做的事，再按任务授予对应权限。小企业最后通常落在四到五个角色上：

| 角色 | 典型权限 | 明确划在范围之外 |
|---|---|---|
| 所有者 | 全部权限，包括账单、角色管理与数据导出 | 系统内无禁区，因此这个角色要保持稀少 |
| 经理 | 审批订单与退款、调整排期、查看报表 | 账单设置与角色管理 |
| 员工 | 新建与编辑日常记录、处理分派给自己的客户 | 退款、导出与删除共享记录 |
| 财务 | 发票、收款、对账与财务报表 | 服务设置与客户消息 |
| 外部协助 | 一个具名模块，限项目期内使用 | 该模块之外的一切 |

有两条设计原则能让这张表不流于形式。第一，每个角色从空白起步，按任务逐项挣得权限，授予因此始终经过斟酌。第二，一个人只持有能覆盖其工作的最小角色集合。比如一位同时兼答客服工单的记账员，就持有财务角色加一个受限的客服角色，每个角色都窄到能用一句话说清。

## 登录回答「是谁」，权限回答「能做什么」

角色权限与登录是配套关系，互相替代不了。统一账户告诉系统键盘前坐的是谁，角色决定这个人能打开、编辑、审批或删除什么。我们此前关于[一个账户用遍全部产品](2026-11-20-unified-sign-in-one-account.md)的文章讲的是这对关系里身份的那一半。权限这一半同样值得认真对待，因为一个身份无误却权限过大的登录，照样会让企业暴露在风险里。两半都到位时，员工登录一次，看到的是岗位需要的工具，走到别人岗位的边界时，会遇上一道清楚的拦截。

## 一页权限矩阵就是工作文件

矩阵是一张朴素的表格：行是操作，列是角色，允许的位置打上标记。把它做出来，只需要和经营者开一次专注的会。一套可行的顺序是：

1. 先列出带风险的操作：付款、退款、改价、数据导出、删除记录、用户管理与设置变更。
2. 逐项过一遍角色，标明谁可以执行、谁可以审批、谁应当完全不参与。
3. 标出需要第二个人参与的操作，比如超过设定金额的退款，或银行账户信息的变更。
4. 把矩阵存到团队找得到的地方，附上日期和负责人。

之后系统配置就照着矩阵来。每处设置都与表格核对，对不上的地方，要么改设置，要么把矩阵里那一行拿出来公开讨论。无论哪种结果，决定都落在纸面上，而权限决定正应该待在纸面上。

## 入职、转岗、离职，让角色跟上人员变化

人变了而系统不变，角色就会慢慢走样。一套与人事变动挂钩的简短例行动作，能让名单保持准确：

- **入职**：第一天建好账户，按矩阵分配角色，并记录由谁批准了这次分配。
- **转岗**：岗位变化时，在加上新角色的同一步里移除旧角色，让上一个岗位的权限按期退场。
- **离职**：在最后一个工作日停用账户，把其名下记录的所有权转给具名同事，并排查需要轮换的共用凭证。

共用账户会把上面这一切架空，因为共用登录下的操作谁也认领不了。确实有工具强制共用登录，比如老式的供应商门户，那就把持有凭证的人记下来，凭证存进公司的密码管理器，持有人离职时立即轮换。例外要摆在明处、有人管理，而不是悄悄被遗忘。

## 按日历复核，也读一读现成的日志

每季度复核一次，能让这套设计贴近现实。所有者或经理把角色名单打印出来，逐个名字对照当前岗位，移除已经对不上的权限。同一次复核里，再抽查敏感操作的活动日志：导出、删除、权限变更。大多数小系统本来就在记录这些事件，复核要做的只是指定一个人去读。发现的问题回写进矩阵，矩阵换上新日期。

权限工作在日常增长中也有回报。新功能上线前先问一句哪些角色能用它，落地会稳妥得多，因为这个问题逼着团队先定下新能力归谁负责。KINGAI 在 [kingai.work](https://kingai.work) 背后的企业系统工作中就采用这种权限先行的做法，把角色设计放进初始搭建，而不是留作事后清理。小企业用不大的代价就能采用同样的次序：一张矩阵、四五个角色、每个季度一次日历提醒。

---

*由 kingai.work 提供技术支持*
