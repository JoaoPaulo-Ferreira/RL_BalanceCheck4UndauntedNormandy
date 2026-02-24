# 🎲 UndauntedLab — AI-Driven Tactical Wargame Simulation

> An **AI, Simulation, and Reinforcement Learning** research engine for *Undaunted: Normandy*, focused on one core question:  
> **Is scenario X fair, or does one side have a systematic statistical advantage?**

This project combines:
- **Game engine engineering**
- **Deterministic simulation**
- **AI agents & Reinforcement Learning**
- **Large-scale statistical analysis**
- **Reproducible experiments**

The long-term goal is to:
- Build a **deterministic, testable, text-based simulation engine**
- Make the game fully **playable via terminal**
- Plug in **AI agents (heuristic + RL)**
- Run **thousands of simulations** to measure balance, bias, and variance
- Turn subjective balance discussions into **data-driven conclusions**

This repository is both:
- A **portfolio-grade AI & simulation project**
- A **research playground** for decision-making systems
- A **showcase of software architecture, testing, and reproducibility**

---

## 🧠 Why This Project?

This project touches multiple high-value areas for AI / engineering roles:

- ✔️ Simulation engines & environments  
- ✔️ Reinforcement Learning & self-play  
- ✔️ Game state modeling & action spaces  
- ✔️ Deterministic systems & reproducibility  
- ✔️ Statistical analysis of experiments  
- ✔️ Clean architecture & testable code  
- ✔️ Research-oriented engineering mindset  

Think of it as:
> A **custom RL environment + game engine + experiment framework** for tactical, turn-based decision making.

---

## 🧭 Guiding Principles

- First make it **work**
- Then make it **playable**
- Then make it **smart (AI)**
- Then make it **scientific (statistics & analysis)**
- Deterministic, testable, reproducible > fancy visuals
- Text-only comes before any AI

---

## 🗂️ High-Level Architecture (Draft)

- `engine/` → Game loop, rules, state transitions  
- `map/` → Tiles, terrain, paths, line-of-sight  
- `units/` → Units, stats, states, combat models  
- `cards/` → Cards, decks, hands, action generation  
- `rules/` → Validation, invariants, legality checks  
- `ui_text/` → Text-based interface (human-playable)  
- `agents/` → Random, heuristic, and RL agents  
- `sim/` → Simulation runners, experiments, statistics  
- `analysis/` → Metrics, plots, reports  

---

## 🏗️ Phase 1 — Environment & Map Engine (Simulation Core)

**Goal:** Build the spatial and geometric foundation of the environment.

### Core Classes (Draft)

- `Tile`
  - `terrain_type`, `neighbors`
  - `is_passable(unit_type)`
  - `movement_cost(unit_type)`
  - `defense_modifier()`

- `Map`
  - `tiles`
  - `get_tile(id)`
  - `are_adjacent(a, b)`
  - `load_from_file(path)`

- `Pathfinder`
  - `find_paths(start, end)`
  - `shortest_path(start, end, unit_type)`
  - `path_cost(path, unit_type)`

- `LineOfSight`
  - `has_los(a, b, map)`

### Landmarks

- [X] Represent generic map and tiles  
- [X] Represent objective points
- [X] Represent scoutted tiles
- [X] Load scenario maps from data files  
- [X] Compute minimal paths between tiles  
- [X] Compute distance defence + terrain defense between tiles  


**Exit criteria:**  
✔️ The environment can answer: *Can I move there? How far? What’s the defense here?*

---

## 🪖 Phase 2 — Units, Dice, and Core Mechanics (Game Physics)

**Goal:** Implement the deterministic “physics” of the game world.

### Core Classes

- `Die`
  - `roll()`
  - `roll_n(n)`  
  - (Seedable for reproducible experiments)

- `Unit`
  - `id`, `unit_type`, `team`, `hp`, `position`, `state`
  - `can_move()`
  - `can_attack()`
  - `apply_damage(amount)`
  - `apply_suppression()`
  - `is_alive()`

- `CombatResolver`
  - `resolve_attack(attacker, defender, game_state)`
  - `compute_dice_pool(attacker, defender, distance, terrain)`
  - `apply_results(result, attacker, defender)`

- `MovementResolver`
  - `can_move(unit, path)`
  - `move_unit(unit, path)`

### Landmarks

- [ ] Implement deterministic, seedable RNG  
- [ ] Implement base `Unit` abstraction  
- [ ] Implement unit types (Rifleman, Scout, MG, Mortar, etc.)  
- [ ] Implement damage, suppression, elimination  
- [ ] Implement attack resolution  
- [ ] Implement movement resolution  
- [ ] Unit tests for combat and movement  

**Exit criteria:**  
✔️ The simulator can resolve interactions like: *“Unit A attacks unit B”* deterministically.

---

## 🃏 Phase 3 — Cards, Decks, and Action Space

**Goal:** Model the **decision-making layer** of the game (critical for AI).

### Core Classes

- `Card`
  - `id`, `name`, `card_type`
  - `get_possible_actions(game_state, player)`

- `UnitCard(Card)`  
- `CommanderCard(Card)`  
- `AdjunctCard(Card)`  

- `Deck`
  - `draw_pile`, `discard_pile`
  - `draw(n=1)`
  - `discard(card)`
  - `reshuffle()`

- `Hand`
  - `cards`
  - `add(card)`
  - `remove(card)`
  - `list_playable(game_state)`

- `Action`
  - `is_legal(game_state)`
  - `apply(game_state)`

### Landmarks

- [ ] Implement card hierarchy  
- [ ] Implement deck / hand / discard  
- [ ] Implement draw and reshuffle  
- [ ] Implement conditional action generation  
- [ ] Implement action legality checks  
- [ ] Unit tests for action generation  

**Exit criteria:**  
✔️ The game exposes a **well-defined action space** for humans and AI agents.

---

## 🎮 Phase 4 — Game State, Rules, and Loop

**Goal:** Turn the engine into a full **MDP-like environment** (Markov Decision Process).

### Core Classes

- `GameState`
  - `map`, `units`, `players`, `decks`, `hands`, `current_player`
  - `clone()`
  - `is_terminal()`
  - `get_winner()`

- `RuleEngine`
  - `list_legal_actions(game_state, player)`
  - `validate_action(action, game_state)`
  - `apply_action(action, game_state)`

- `Scenario`
  - `initial_map`, `initial_units`, `initial_decks`, `victory_conditions`
  - `setup_game()`

- `GameLoop`
  - `step(action)`
  - `run_until_end()`

### Landmarks

- [ ] Implement turn structure  
- [ ] Implement control point rules  
- [ ] Implement victory conditions  
- [ ] Implement scenario loading  
- [ ] Implement action logging  
- [ ] Integration tests with scripted players  

**Exit criteria:**  
✔️ The environment supports **full episodes** from start to terminal state.

---

## 🖥️ Phase 5 — Text-Only Interface (Human Baseline)

**Goal:** Make the environment fully playable by humans for debugging and validation.

### Core Classes

- `TextRenderer`
  - `render_map(game_state)`
  - `render_units(game_state)`
  - `render_hand(player)`

- `CommandParser`
  - `parse(input_str) -> Action`

- `TextGameUI`
  - `prompt_player(player)`
  - `run_game()`

### Landmarks

- [ ] Text rendering of map and units  
- [ ] Command parsing  
- [ ] Show legal actions  
- [ ] Deterministic mode (fixed seed)  
- [ ] Save/load game state  
- [ ] Replay from logs  

**Exit criteria:**  
✔️ Two humans can play end-to-end using only the terminal.

---

## 🤖 Phase 6 — AI Agents & Reinforcement Learning

**Goal:** Turn the engine into an **AI research environment**.

### Core Classes

- `Agent`
  - `select_action(game_state)`

- `RandomAgent`, `HeuristicAgent`, `RLAgent`

- `StateEncoder`
  - `encode(game_state)`

- `TrainingLoop`
  - `self_play()`
  - `train_step()`
  - `evaluate()`

### Landmarks

- [ ] Define state representation  
- [ ] Define action encoding  
- [ ] Implement baseline agents  
- [ ] Implement self-play  
- [ ] Integrate RL algorithm (PPO / DQN / etc.)  
- [ ] Track learning curves and metrics  

---

## 📊 Phase 7 — Statistical Analysis & Balance Evaluation

**Goal:** Perform **data-driven scenario balance analysis**.

### Core Classes

- `SimulationRunner`
  - `run_n_games(n, scenario, agent_a, agent_b)`

- `ResultsAnalyzer`
  - `win_rate_by_side()`
  - `confidence_intervals()`
  - `first_player_advantage()`

- `ReportGenerator`
  - `generate_plots()`
  - `export_report()`

### Landmarks

- [ ] Large-scale simulations  
- [ ] Win-rate computation  
- [ ] RNG sensitivity analysis  
- [ ] Agent skill comparison  
- [ ] Plots and reports per scenario  

---

## 🎯 Final Objective

Turn:

> “This scenario feels unbalanced”

into:

> “Under these assumptions, with these agents, side A wins **X ± Y %** of games over N simulations.”

---

## 📌 Project Status

- [ ] Phase 1 — Ongoing
- [ ] Phase 2 — Not started  
- [ ] Phase 3 — Not started  
- [ ] Phase 4 — Not started  
- [ ] Phase 5 — Not started  
- [ ] Phase 6 — Not started  
- [ ] Phase 7 — Not started  

---

**Keywords:** Simulation, Game Engine, AI, Reinforcement Learning, Decision-Making, Self-Play, Reproducibility, Statistical Analysis, Research Engineering
