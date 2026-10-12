[README.md](https://github.com/user-attachments/files/33330779/README.md)
# 債衝刺 Bond Dash：即時多人賽跑

最多 8 人同時開跑，狂點按鈕往前衝。途中會遇到 Fed 升降息和配息補給站答題，成績登記到所有房間共用的全站排行榜。

## 檔案說明

| 檔案 | 用途 |
|---|---|
| `app.py` | Streamlit 主程式，負責把 Supabase 金鑰交給遊戲 |
| `game.html` | 遊戲本體（題庫、跑鞋、賽道長度都在最上面的「設定區」） |
| `requirements.txt` | 套件清單 |
| `schema.sql` | 在 Supabase 建立排行榜資料表的指令 |

## 部署步驟（約 10 分鐘）

### 1. Supabase：建立排行榜資料表
1. 登入 Supabase，打開你之前遊戲用的那個專案（共用同一個就可以）
2. 左側選單點「SQL Editor」→「New query」
3. 把 `schema.sql` 的內容整段貼上，按「Run」
4. 出現 Success 就完成了

> 即時同步（大家一起跑）用的是 Supabase 內建的 Realtime 功能，不用另外設定。

### 2. GitHub：新開一個 repo
1. 到 GitHub 按「New repository」，名字可以取 `bond-dash`
2. 把這 4 個檔案上傳上去（Add file → Upload files）

### 3. Streamlit Cloud：部署
1. 到 share.streamlit.io 按「Create app」，選剛剛的 repo，主程式填 `app.py`
2. 到「Advanced settings」→「Secrets」，貼上（換成你自己的值，跟之前遊戲一樣）：
   ```
   SUPABASE_URL = "https://xxxxx.supabase.co"
   SUPABASE_ANON_KEY = "eyJhbGciOi..."
   ```
3. 按 Deploy，完成！

## 怎麼玩
- 一個人按「開一個新房間」，畫面上會出現 4 碼房號，把房號告訴大家
- 其他人輸入房號加入（也可以直接分享網址 `你的網址/?room=房號`，房號會自動填好）
- 每個人選好債券跑鞋，房主按「開跑」，大家同時倒數 3、2、1
- 人數不夠時，房主可以加「電腦跑者」湊數（電腦的成績不會上排行榜）

## 常見調整
在 `game.html` 最上面的「設定區」：
- **改題目**：修改 `QUESTIONS`，每題的第一個選項要放正確答案（畫面上會自動打亂順序）
- **改賽道長度**：`RACE_M`（預設 200 公尺，一場約 30 秒）
- **改補給站位置**：`STATIONS`
- **改房間人數上限**：`MAX_PLAYERS`

## 小提醒
- 還沒設定 Supabase 時，遊戲會進入「本機示範模式」：在同一台電腦開多個分頁就能測試多人，成績只存在自己的瀏覽器裡
- Supabase 免費方案的即時訊息有每秒上限。如果內訓時同時開很多房間，覺得有點卡，可以請大家分批開跑
- Streamlit 免費方案閒置太久會休眠。正式活動前，記得先自己打開網址把它喚醒
