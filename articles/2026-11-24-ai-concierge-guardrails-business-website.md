# AI Concierge for Business Websites: Guardrails That Keep Answers Within Approved Facts
## 企业网站的 AI 客服：用护栏把回答限定在已核准事实内

> **TL;DR:** An AI concierge earns its place on a business website when it answers routine questions after hours from an approved answer library. Prices come only from published pages, availability comes only from a live booking feed, and every topic outside the library routes to a named staff member with a due time. A written zone table, a prepared fallback sentence, and weekly log reviews keep the concierge helpful at midnight and accountable the next morning.

## The midnight question is a real inquiry

A visitor who lands on a service site at 11:40 p.m. usually asks plain questions: which areas the business covers, what a service includes, and how booking works. Staff are offline at that hour, so the choice on the page is between a guarded concierge and a silent contact form. A guarded concierge answers the plain questions on the spot, from material the business has already approved for publication. Questions that need judgment wait in a queue with a named owner, and the visitor leaves knowing when a person will pick the thread up. That division of labour is the whole design. Everything else in this article supports it.

## Build the answer library before the chat window

The concierge answers from a library, and the library comes first. Source material is the published site itself: service pages, the service area list, opening hours, booking steps, and policy wording the business already stands behind. Each library entry carries an owner and a review date, so stale wording has a person responsible for refreshing it. Entries that pass their review date drop out of the answer set until the owner confirms them again. The concierge retrieves answers from this library at answer time. General background knowledge may shape the phrasing of a reply, while facts about the business come from the library alone. Teams that skip this stage end up proofreading chatbot output every morning, which often costs more time than writing the library once.

## Sort topics into handling zones

A zone table settles most behaviour questions before launch. The team writes the table once, reviews it when services change, and tests the concierge against it.

| Topic | The concierge may | Hand off when |
|---|---|---|
| Services and coverage | Describe published services and listed areas | The visitor asks about an unlisted service or area |
| Prices | Quote published prices word for word, with a link to the source page | The visitor asks for a discount, a bundle, or a special case |
| Scheduling | Show booking steps and open slots from the live booking feed | The feed is unavailable, or the visitor needs a time outside it |
| Policies and exceptions | State published policy wording | The visitor requests a deadline commitment, a refund exception, or a custom term |
| Complaints and disputes | Record the details and flag the thread as priority | Always: a person owns the reply from the first message |

## Prices and promises need hard edges

Money topics are where improvisation does real damage, so the rules here stay blunt. The concierge quotes a number only when that number appears in the library, and it keeps any qualifier attached, so a starting price stays a starting price. Discounts, bundles, and negotiated terms belong to staff, full stop. Availability follows the same pattern: open slots come from the booking feed, and when the feed cannot be reached, the concierge says the schedule needs a human check and offers the handoff. Completion dates, guaranteed response times beyond the published window, and outcome claims stay outside the concierge's vocabulary. When a question crosses a zone boundary, a prepared fallback sentence carries the moment: "That detail sits outside the published information I can quote here. I can pass your question to the team with your contact details, and they will reply within the window shown on our contact page." The sentence is polite, accurate, and final, which is exactly what a boundary needs to be.

## Design the handoff as carefully as the answers

A handoff collects four things: a name, a contact route, the topic in the visitor's own words, and a short summary the concierge drafts for staff. The thread then lands in the same queue discipline as any other inquiry, with an owner and a due time attached. Our earlier note on [contact forms as queues](2026-11-18-contact-form-queue-routing.md) lays out that routing pattern in detail, and it applies to chat threads unchanged. The visitor sees a confirmation that names the published response window, for example the next business morning for a standard inquiry. Priority topics follow a faster lane: a billing dispute or a safety concern gets a priority flag in the queue, and the concierge also displays the phone number for anyone who would rather call. A concierge that hands off gracefully keeps trust on the nights when the honest answer is "a person will handle this."

## Test with awkward questions before launch

Launch readiness comes from a test set, and awkward questions make the best tests. Before going live, staff work through a written list and record the expected behaviour beside each question:

- Ask for a discount the site has never offered, and check the reply hands off instead of inventing a figure.
- Ask about a service area the business has never covered.
- Ask for a guaranteed completion date.
- Ask the same price question three ways, and confirm the quoted figure stays identical.
- Paste a long, unrelated document and ask about it; the concierge should stay on business topics.
- Ask a question the library genuinely lacks, and confirm the handoff collects contact details.

Each failure points at a specific fix: a missing library entry, a zone that needs a clearer boundary, or a fallback sentence that needs rewriting. After launch, a weekly review of sampled conversations keeps the library honest. Reviewers tag unanswered topics, correct entries that drifted from the published pages, and add the questions visitors actually asked. KINGAI builds this kind of guarded concierge setup in the intelligent website work behind [kingai.work](https://kingai.work), where an approved answer library and a staffed queue run as one system. A business running its own setup can start smaller: one service page, one zone table, and ten awkward test questions will surface most of the gaps worth fixing.

---

*Technical support by kingai.work*

---

# 企业网站的 AI 客服：用护栏把回答限定在已核准事实内

> **摘要**：AI 客服在企业网站上站得住脚，靠的是夜间也能从已核准的答案库里回答常规问题。价格只引用已发布页面，可约时间只来自实时预约通道，答案库之外的话题一律转给具名负责人并附处理时限。一张写明的分区表、一句预备好的兜底话术、每周一次的对话记录复查，能让它半夜帮上忙，第二天早上也交代得清楚。

## 半夜的问题也是正经咨询

晚上 11 点 40 分落到服务类网站上的访客，问的通常都是直白的问题：业务覆盖哪些区域、一项服务包含什么、预约怎么操作。这个时段员工已经离线，页面上的选择就是有护栏的 AI 客服，或者一张沉默的联系表单。有护栏的客服能当场答掉直白问题，依据是企业已经核准发布的内容。需要人来判断的问题则进队列等候，挂具名负责人，访客离开页面时清楚知道什么时候会有人接手。这套分工就是整个设计的骨架，本文其余部分都在支撑它。

## 先建答案库，再开聊天窗

客服的回答来自答案库，所以答案库要排在前面。素材就是网站已发布的内容本身：服务页面、服务区域清单、营业时间、预约步骤，以及企业已经对外承诺过的政策措辞。每条答案都挂负责人和复核日期，措辞过期时有人负责更新。过了复核日期的条目先退出可答范围，等负责人重新确认后再回来。客服在回答时从库里调取答案。通用背景知识可以影响回复的措辞，而涉及这家企业的事实只从库里来。跳过这一步的团队，最后会变成每天早上给聊天机器人改稿，往往花的时间比一开始把答案库写好更多。

## 把话题分进处理区

一张分区表能在上线前把大多数行为问题定下来。团队写一次，服务有变化时复核，并拿客服对照着测。

| 话题 | 客服可以做 | 出现这些情况时转人工 |
|---|---|---|
| 服务与覆盖 | 介绍已发布的服务与已列明的区域 | 访客问到未列明的服务或区域 |
| 价格 | 逐字引用已发布价格，并附来源页面链接 | 访客要求折扣、套餐或特殊个案 |
| 预约 | 展示预约步骤与实时预约通道里的空位 | 通道不可用，或访客需要通道之外的时间 |
| 政策与例外 | 照已发布政策原文陈述 | 访客要求工期承诺、退款例外或定制条款 |
| 投诉与争议 | 记录详情并把该线索标为优先 | 一律转人工：从第一条回复起就由人负责 |

## 价格与承诺要有硬边界

涉及钱的话题最怕临场发挥，所以这里的规矩写得直白。客服只引用出现在答案库里的数字，并保留数字附带的条件，比如起价就还是起价。折扣、套餐和议价条款归员工处理，没有例外。可约时间同理：空位来自预约通道，通道连不上时，客服就说明排期需要人工核对，并提供转人工的入口。完成日期、超出已发布时限的响应保证、效果类说法，都不在客服的词表里。问题越过分区边界时，一句预备好的兜底话术就能接住场面：「这项细节超出了我在这里能引用的已发布信息范围。我可以把您的问题连同联系方式转给团队，他们会在联系页所示的时限内回复。」这句话礼貌、准确、不留口子，边界需要的正是这个效果。

## 转人工要和回答本身一样认真设计

一次合格的转接要收集四样东西：姓名、联系方式、访客原话里的问题主题，以及客服为员工起草的一段简短摘要。线索随后进入与普通咨询相同的队列纪律，挂负责人、附处理时限。我们此前关于[联系表单按队列管理](2026-11-18-contact-form-queue-routing.md)的文章详细写过这套分流方式，用到聊天线索上原样适用。访客会看到一条确认信息，写明已发布的响应时限，例如普通咨询在下一个工作日上午处理。优先话题走更快的通道：账单争议或安全类问题在队列里标为优先，客服同时显示电话号码，方便愿意直接来电的人。转接做得体面，客服就能在那些诚实答案是「这件事由人来办」的夜晚守住信任。

## 上线前先拿别扭问题测一轮

能不能上线，看一套测试题，而别扭问题是最好的测试题。正式开放前，员工逐条跑完一份书面清单，并在每个问题旁写明预期行为：

- 要求一个网站从未给过的折扣，检查回复是否转人工，有没有编出数字。
- 问一个企业从未覆盖过的服务区域。
- 要求保证某个完成日期。
- 同一个价格问题换三种问法，确认引用的数字始终一致。
- 粘贴一份很长的无关文档并就它提问；客服应守在业务话题内。
- 问一个答案库里确实没有的问题，确认转接会收下联系方式。

每次失败都指向一个具体修法：答案库缺一条、某个分区的边界要写得更清楚，或者兜底话术需要重写。上线后，每周抽查一次对话记录，答案库才不会慢慢跑偏。复查的人给未答出的话题打标，修正与已发布页面脱节的条目，再把访客真正问过的问题补进去。KINGAI 在 [kingai.work](https://kingai.work) 背后的智慧网站工作中搭建这类有护栏的客服配置，让已核准的答案库与有人值守的队列作为一套系统运行。自己搭建的企业可以从更小的规模起步：一页服务说明、一张分区表、十道别扭测试题，就能把值得修的缺口暴露出大半。

---

*由 kingai.work 提供技术支持*
