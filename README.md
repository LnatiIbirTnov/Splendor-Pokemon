# Splendor Pokemon 桌游框架

这是一个用于 **Splendor Pokemon 版本桌游** 的代码框架，目标是为后续接入 AI agent 做准备。
当前实现聚焦在 **领域模型、规则入口、状态管理与 AI 接口** 的骨架设计，方便后续扩展卡牌、角色、规则与训练逻辑。

## 目录结构

```
splendor_pokemon/
  agents/            # AI 代理接口与基类
  models/            # 核心领域模型（卡牌、玩家、棋盘、代币等）
  actions.py         # 玩家动作定义
  game.py            # 游戏引擎入口
  observation.py     # AI 观测定义
  rules.py           # 规则与合法性验证
  types.py           # 共享枚举与类型
  utils/             # 通用工具（预留）
```

## 目标特性

- ✅ 完整的领域对象建模（玩家、卡牌、代币、棋盘）
- ✅ 可扩展的动作系统（拿取、预定、购买、过牌）
- ✅ AI 接口：Agent 可根据 Observation 选择 Action
- ✅ 规则引擎入口：集中处理合法性与胜利判定
- ✅ GameEngine：统一推进回合、生成合法动作、更新状态

## 后续计划（可扩展方向）

- 接入完整 Splendor 规则与 Pokemon 主题卡牌
- 增加训练环境（Gym 风格）与对局回放
- 加入可视化/日志系统
- 定义配置化卡池、精灵与训练师能力

---

欢迎在此基础上逐步扩展：你只需要补全 `rules.py` 和 `models/` 中的细节，就能逐步形成完整玩法。
