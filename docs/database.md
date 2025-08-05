以下に、**簡易タスク管理アプリ**のための\*\*データベース設計（ER図）\*\*と各テーブルの詳細を示します。
対象は **シングルユーザーおよびチーム対応前提**で、認証・管理機能も想定しています。

---

## ✅ ER図（Entity Relationship Diagram）

```
+-----------+        1        N      +----------+
|  users    |----------------------<|  tasks   |
+-----------+                       +----------+
| id        |                       | id       |
| username  |                       | title    |
| email     |                       | detail   |
| password  |                       | status   |
| is_admin  |                       | due_date |
| created_at|                       | priority |
| updated_at|                       | owner_id |
+-----------+                       | created_at|
                                    | updated_at|
                                    +-----------+
```

---

## ✅ テーブル定義

---

### 🟦 `users` テーブル

| カラム名         | 型              | 制約               | 説明            |
| ------------ | -------------- | ---------------- | ------------- |
| `id`         | `UUID`         | PK               | ユーザーID（主キー）   |
| `username`   | `VARCHAR(50)`  | UNIQUE, NOT NULL | 表示名           |
| `email`      | `VARCHAR(100)` | UNIQUE, NOT NULL | ログイン用メールアドレス  |
| `password`   | `TEXT`         | NOT NULL         | ハッシュ化されたパスワード |
| `is_admin`   | `BOOLEAN`      | DEFAULT FALSE    | 管理者フラグ        |
| `created_at` | `TIMESTAMP`    | DEFAULT NOW()    | 登録日時          |
| `updated_at` | `TIMESTAMP`    | DEFAULT NOW()    | 更新日時（自動更新）    |

---

### 🟩 `tasks` テーブル

| カラム名         | 型              | 制約             | 説明                 |
| ------------ | -------------- | -------------- | ------------------ |
| `id`         | `UUID`         | PK             | タスクID（主キー）         |
| `title`      | `VARCHAR(100)` | NOT NULL       | タスクタイトル            |
| `detail`     | `TEXT`         | NULLABLE       | タスク詳細              |
| `status`     | `VARCHAR(10)`  | NOT NULL       | `todo` / `done` など |
| `due_date`   | `DATE`         | NULLABLE       | 締切日（任意）            |
| `priority`   | `INTEGER`      | DEFAULT 0      | 優先度（0:低〜3:高など）     |
| `owner_id`   | `UUID`         | FK -> users.id | 作成者                |
| `created_at` | `TIMESTAMP`    | DEFAULT NOW()  | 作成日時               |
| `updated_at` | `TIMESTAMP`    | DEFAULT NOW()  | 更新日時（自動更新）         |

---

## ✅ リレーションの詳細

| 関係                    | 内容                                                   |
| --------------------- | ---------------------------------------------------- |
| `users` 1 → N `tasks` | 1人のユーザーは複数のタスクを持てる（`owner_id` により紐付け）                |
| 外部キー制約                | `tasks.owner_id` → `users.id`（ON DELETE CASCADE を推奨） |

---

## ✅ インデックス設計（パフォーマンス最適化）

| テーブル    | カラム                              | インデックスの目的     |
| ------- | -------------------------------- | ------------- |
| `users` | `email`                          | ログイン処理の高速化    |
| `tasks` | `owner_id`, `status`, `due_date` | 一覧・フィルタ処理の最適化 |

---

## ✅ 補足（今後の拡張可能性）

| 拡張例    | 方法                                      |
| ------ | --------------------------------------- |
| タグ管理   | `task_tags` テーブルを追加し、多対多関係              |
| コメント機能 | `comments` テーブルを追加                      |
| チーム対応  | `teams`, `user_teams` テーブル追加でチーム・メンバー管理 |

---

必要であれば、このER図に基づく **SQL DDL定義** や **SQLAlchemy モデル定義** も即時提供可能です。ご指定ください。
