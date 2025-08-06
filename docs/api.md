以下は、**簡易タスク管理アプリ**に必要な REST API エンドポイント一覧とその詳細仕様です。

各エンドポイントは **認証トークン（JWT）前提** で、基本的に `/api/v1/` プレフィックスがついています。

---

## ✅ API 一覧

| メソッド | エンドポイント      | 概要                       |
| -------- | ------------------- | -------------------------- |
| POST     | `/auth/register`    | ユーザー登録               |
| POST     | `/auth/login`       | ログイン（JWT 発行）       |
| GET      | `/auth/me`          | ログイン中ユーザー情報取得 |
| GET      | `/users`            | （管理者）全ユーザー一覧   |
| GET      | `/tasks`            | 自分のタスク一覧取得       |
| GET      | `/tasks/:id`        | 単一タスクの取得           |
| POST     | `/tasks`            | タスク作成                 |
| PUT      | `/tasks/:id`        | タスク編集                 |
| PATCH    | `/tasks/:id/status` | 完了状態切り替え           |
| DELETE   | `/tasks/:id`        | タスク削除                 |
| GET      | `/admin/tasks`      | （管理者）全タスク一覧     |

---

## ✅ エンドポイント詳細仕様

---

### 🔐 `POST /auth/register`

- ユーザー登録

**リクエスト:**

```json
{
  "username": "taro",
  "email": "taro@example.com",
  "password": "password123"
}
```

**レスポンス:**

```json
{
  "id": "uuid",
  "username": "taro",
  "email": "taro@example.com"
}
```

---

### 🔐 `POST /auth/login`

- 認証・トークン発行

**リクエスト:**

```json
{
  "email": "taro@example.com",
  "password": "password123"
}
```

**レスポンス:**

```json
{
  "access_token": "jwt_token",
  "token_type": "bearer"
}
```

---

### 🔐 `GET /auth/me`

- 自分のユーザー情報取得（JWT 必須）

**レスポンス例:**

```json
{
  "id": "uuid",
  "username": "taro",
  "email": "taro@example.com",
  "is_admin": false
}
```

---

### 👤 `GET /users` （管理者専用）

- 全ユーザー一覧（管理画面用）

---

### 📋 `GET /tasks`

- 自分のタスク一覧取得（フィルタ付き）

**クエリ例:**

```
/tasks?status=done&priority=2&due_before=2025-12-31
```

**レスポンス:**

```json
[
  {
    "id": "uuid",
    "title": "企画書作成",
    "status": "done",
    "priority": 2,
    "due_date": "2025-08-10"
  }
]
```

---

### 📄 `GET /tasks/:id`

- 単一タスク詳細取得

---

### ➕ `POST /tasks`

- タスク作成

**リクエスト:**

```json
{
  "title": "レポート提出",
  "detail": "明日までに提出",
  "due_date": "2025-08-06",
  "priority": 1
}
```

---

### ✏️ `PUT /tasks/:id`

- タスク内容を全面更新

**リクエスト:**

```json
{
  "title": "資料提出",
  "detail": "顧客向けのプレゼン資料",
  "status": "todo",
  "due_date": "2025-08-08",
  "priority": 3
}
```

---

### ✅ `PATCH /tasks/:id/status`

- 完了マークの切り替え専用

**リクエスト:**

```json
{
  "status": "done"
}
```

---

### ❌ `DELETE /tasks/:id`

- タスク削除

---

### 🛠️ `GET /admin/tasks`（管理者専用）

- すべてのユーザーのタスク一覧取得

**クエリ例:**

```
/admin/tasks?user_id=abc-123&status=todo
```

---

## ✅ エラーレスポンス（共通）

- 認証失敗 → `401 Unauthorized`
- 権限不足 → `403 Forbidden`
- リソース未存在 → `404 Not Found`
- バリデーションエラー → `422 Unprocessable Entity`

---

## ✅ 認証

すべての `/tasks` 系エンドポイントでは `Authorization: Bearer <JWT>` を要求します。

---

必要であれば：

- OpenAPI 仕様（YAML / JSON）
- FastAPI ルーティング実装
- Axios API ラッパー（Vue.js）

を作成できます。次に進める項目をご指定ください。
