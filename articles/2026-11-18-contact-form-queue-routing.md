# Your Contact Form Is a Queue: Routing Inquiries With Owners, Due Times, and Daily Review

> **TL;DR** — A contact form that only sends an email creates a shared inbox problem: messages wait unread, two people reply to the same inquiry, or nobody replies at all. Treating the form as a queue fixes ownership first. Each submission gets a category, a named owner, a due time, and a visible status. Simple routing rules and a short daily review can run on tools a small business already has.

A website contact form looks simple from the outside. A visitor fills in a few fields, presses send, and expects an answer. Inside the business, that submission often lands as one more email in a mailbox several people share and nobody fully owns. The form itself worked. The handling after it did not.

The fix starts with a change in model. A mailbox stores messages. A queue moves work. A queued submission carries enough information to be assigned, tracked, and closed, rather than relying on someone remembering to check a folder.

## Why inquiries die in a shared inbox

Inquiries get lost for ordinary, fixable reasons. The notification arrives during a busy period and scrolls out of view. A staff member reads it, assumes a colleague will answer, and marks nothing. A question needing input from two people stalls because the first reader cannot complete it alone. Spam filters catch a legitimate message, and nobody reviews the filtered folder.

None of these failures needs a large system. They need a record outside any one person's inbox, plus a routine for looking at it. If the only copy of an inquiry is an email, the business cannot reliably answer a basic question: which submissions are still waiting?

## Give every submission four things at intake

A queue entry should be useful on arrival. Four fields do most of the work.

**A category the visitor chooses.** Offer a short list such as new project, existing order, billing question, problem report, partnership, or other. Self-selected categories are usually close enough to route by, and staff can correct the label later.

**Contact details with one required reply channel.** Ask for an email address or a phone number, and make one required. An inquiry with no reachable sender cannot be answered.

**A free-text field with a guiding prompt.** A prompt such as "What are you trying to get done, and by when?" produces more useful messages than a blank box.

**An automatic timestamp and status.** The system should record when the submission arrived and set its first status to new. Later statuses (in progress, waiting on visitor, answered, closed) turn a pile of messages into a list a manager can scan quickly.

## Route by category

Routing works when each category has a named owner and a backup. The table below is a starting pattern a small team can adapt quickly.

| Category | First owner | Backup | First response due |
| --- | --- | --- | --- |
| New project or service inquiry | Owner or sales lead | Office manager | Same business day |
| Existing order or booking | Staff member handling that order | Office manager | Same business day |
| Billing question | Bookkeeper or owner | Office manager | Next business day |
| Complaint or problem report | Owner or senior staff | Named deputy | Same business day, sooner if urgent |
| Partnership or supplier pitch | Owner | Office manager | Within two business days |
| Other or unclassified | Office manager | Owner | Next business day, then reassign |

Two details matter more than the exact times. First, the backup is a person, not a department. Second, unclassified submissions still get an owner whose job is to reassign them. Response times should reflect what the team can keep on a busy week, stated in plain language near the form.

## A daily ten-minute queue review

Queues fail when nobody looks at them. A short review at a fixed time keeps the list honest.

1. Open the queue and sort by status, oldest first.
2. Check every item still marked new and assign or reassign it.
3. Look at items waiting longest in progress and note what each one is blocked on.
4. Close answered items where the visitor has not replied within the period your team agreed.
5. Count how many items arrived, how many closed, and how many are overdue, and write the three numbers in a log.

The review belongs to one named person per day, on a simple rotation if needed. Sorting inquiries is also one of the first tasks an office can hand to supervised automation, a point we covered in [AI Digital Staff for a Small Office](2026-11-17-ai-digital-staff-small-office.md). Whether a person or a tool sorts, the review stays, because it catches the item that fits no rule.

## What automation should do, and where it should stop

Automation fits the mechanical parts of a queue well. It can send an acknowledgement with a reference number and the stated response time, assign a category owner, set a due time, flag overdue items, and prepare draft replies from approved material for routine questions.

Automation should stop at judgment calls. Complaints, requests involving money, messages with a legal deadline, and anything where the visitor is clearly distressed should go to a person with the full submission attached. A draft is fine. Sending without review is where queues start producing confident, wrong answers at speed.

Keep the acknowledgement honest. If the team answers within one business day, say so. If weekends are uncovered, say that too. An accurate expectation reduces follow-up messages that clog the queue further.

## Build it on tools you already have

Most small businesses can run this pattern without new software. A form tool that saves submissions to a table or spreadsheet, rather than only emailing them, already provides the record. Add columns for category, owner, due time, and status, and the spreadsheet becomes the queue view. Email notifications still help, but the record of truth is the table, and the daily review reads the table.

When volume grows, the same structure moves into a help desk system with less pain, because the categories, owners, and statuses already exist. Teams that skip the structure and buy a tool first often end up with a more expensive inbox.

At KINGAIWORK LLC we build inquiry handling this way for intelligent websites and office automation: form, queue record, routing table, and a review routine the team can keep. See [kingai.work](https://kingai.work).

---

*By KINGAIWORK LLC: AI digital staff, intelligent websites and business systems for individuals, companies and public institutions. Technical support by kingai.work · Questions or a project to discuss: vip@kingai.work*

---

# 中文版：联系表单按队列管理：咨询分流、具名负责与每日巡检

> **摘要**：联系表单如果只发一封通知邮件，咨询很容易卡在共用邮箱里：没人看、两个人重复回、或者干脆没人回。把表单当队列来管，先解决的是归属问题。每条提交进来时就带上类别、具名负责人、应答时限和可见状态。再配上简单的分流规则和每天一次的短巡检，小团队用手头已有的工具就能跑起来。

从访客那一侧看，网站联系表单很简单：填几个栏位，点发送，等回复。企业内部却是另一回事。提交往往变成共用邮箱里的一封邮件，好几个人都能看，却没有一个人对它全程负责。表单本身没坏，坏的是提交之后的处理环节。

改法先从换一个看法开始。邮箱是存信的地方，队列是让工作流动起来的地方。咨询进入队列时，身上带着足够的信息，可以被分派、被跟踪、被关闭，全程留在这份记录里。

## 咨询为什么会死在共用邮箱里

咨询丢失的原因都很日常，也都可改。通知邮件在忙的时候到，转眼被新邮件顶下去；一位同事读了，以为另一位会回，什么标记也没留；一个问题需要两个人接力，第一个人答不完，就停在那里；正常咨询被垃圾邮件过滤拦下，而过滤文件夹没人定期看。

这些毛病不需要上大系统才能防住。需要的是一份不依赖某个人收件箱的记录，外加一个固定去看这份记录的动作。咨询的唯一副本只是一封邮件时，企业连一个基本问题都答不上来：现在还有哪些提交在等回复？

## 每条提交在入口处就要备齐四样东西

队列条目一进来就应当可用。四样东西能承担大部分工作。

**由访客自己选的类别。** 给一份短清单，比如新项目、已有订单、账单问题、问题报告、合作洽谈、其他。让访客选，是因为自选类别多数情况下够准、够用来分流，工作人员事后也能改。

**联系方式里至少留一条能回复的渠道。** 邮箱或电话，至少必填一项。写得再清楚的咨询，联系不上提交人，也没法回复。

**带提示语的自由填写栏。** 一句提示，比如「您想办成什么事、希望什么时候办好」，比一个空白框收到的信息有用得多。表单把「一条有用的咨询该写什么」摆出来，访客自然会照着写。

**自动生成的时间与状态。** 系统记录提交到达时间，并把初始状态设为「新建」。之后状态依次流转（处理中、等访客回复、已答复、已关闭），一堆邮件就变成负责人一分钟能扫完的清单。

## 按类别分流

分流能跑通，靠的是每个类别都有具名负责人和替补。下表是一个小团队开一次会就能改用的起步模板。

| 类别 | 第一负责人 | 替补 | 首次回复时限 |
| --- | --- | --- | --- |
| 新项目或服务咨询 | 负责人或销售主管 | 办公室主管 | 同一工作日 |
| 已有订单或预约 | 经办该订单的同事 | 办公室主管 | 同一工作日 |
| 账单问题 | 财务或负责人 | 办公室主管 | 下个工作日 |
| 投诉或问题报告 | 负责人或资深同事 | 指定的副手 | 同一工作日，紧急的更快 |
| 合作或供应商来函 | 负责人 | 办公室主管 | 两个工作日内 |
| 其他或未分类 | 办公室主管 | 负责人 | 下个工作日，并完成转派 |

比具体时限更要紧的是两点。第一，替补要落到具体的人，不能写某个部门。第二，未分类的提交也要有负责人，他的活儿就是把这类提交转派出去，这样说不清的咨询不会落在系统外面。时限要按团队忙时也能守住的水平来定，并用平实的话写在表单旁边，让访客看得见。

## 每天十分钟的队列巡检

队列没人看，就会慢慢失效。固定时间做一次短巡检，清单才保持真实。

1. 打开队列，按状态排序，最老的排在前面。
2. 把还标着「新建」的逐条看过，该分派的分派，该转派的转派。
3. 看处理中停得最久的几条，记下各自卡在什么地方。
4. 访客在团队约定的期限内没有再回复的已答复条目，予以关闭。
5. 数一数当天进来多少条、关闭多少条、逾期多少条，把三个数字记进日志。

巡检每天落到一个具名的人头上，需要时可以轮值。分拣咨询也是办公室最早可以交给受监督自动化的工作之一，我们在[《小办公室的 AI 数字员工》](2026-11-17-ai-digital-staff-small-office.md)里写过这个判断。无论分拣由人做还是工具做，巡检这一步要留住，因为不符合任何规则的那条咨询，靠巡检才能被发现。

## 自动化做到哪一步，停在哪一步

队列里机械性的部分，很适合交给自动化。它可以发一封带编号和承诺回复时限的确认回执；可以按类别分派负责人、设好时限；可以把过了时限还没答复的条目标出来；常规问题，它还能用审定过的材料先备一份回复草稿。

涉及判断的地方，自动化应当停下。投诉、牵涉钱的请求、带法律期限的消息，还有访客明显情绪激动的来信，都应连同完整提交转给具体的人。备草稿可以，不经人看就发出去，队列就会开始高速产出自信而错误的答复。

确认回执要写实话。团队一个工作日内能答复，就这么写；周末没人值守，也写明。预期说准了，后续催问的来信自然少，队列也不容易被催问塞满。

## 用手头已有的工具就能搭起来

多数小企业跑这套办法，不用买新软件。表单工具只要能把提交存进表格、同时发一封通知邮件，记录这一层就有了。表格里再加类别、负责人、时限、状态几列，它就是队列视图。邮件通知仍然有用，提醒负责人有新活儿；但以哪份记录为准，答案是表格，每天巡检看的也是表格。

量再涨上去时，这套结构搬进客服或客户系统也不费劲，因为类别、负责人和状态都已经定好了。跳过结构、先买工具的团队，常常只是买回一个更贵的收件箱。

KINGAIWORK LLC 在为客户搭建智慧网站和办公自动化时，咨询处理就是按这个结构做的：表单、队列记录、分流表，再加一套团队能长期坚持的巡检动作。我们的介绍在 [kingai.work](https://kingai.work)。

---

*KINGAIWORK LLC 出品：AI 数字员工、智慧网站与业务系统，服务个人、企业与公共机构。由 kingai.work 提供技术支持 · 咨询或项目洽谈：vip@kingai.work*
