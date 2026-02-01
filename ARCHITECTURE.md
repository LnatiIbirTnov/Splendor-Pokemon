# 架构说明

本项目采用“核心引擎 + 规则 + AI 接口”的分层设计，方便后续扩展 Splendor Pokemon 的玩法细节。

## 模块分层

- **models/**: 领域模型（玩家、卡牌、棋盘、代币）
- **actions.py**: 玩家动作定义
- **rules.py**: 规则验证与胜利判定入口
- **game.py**: 游戏引擎（负责回合推进、动作执行、状态更新）
- **agents/**: AI 代理接口，提供统一的决策入口
- **observation.py**: 供 AI 观察的状态快照

## AI 接入建议

1. 通过 `GameEngine.observation()` 获取可用于决策的数据
2. 由 `Agent.select_action()` 选择动作
3. 游戏引擎调用 `GameEngine.step(action)` 推进状态

后续可以在 `rules.py` 中加入完整 Splendor 规则、Pokemon 卡牌效果与胜负条件。
