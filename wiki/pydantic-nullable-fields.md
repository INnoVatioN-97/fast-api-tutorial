# Pydantic에서 선택적/Nullable 필드 처리하기

FastAPI와 Pydantic에서 선택적(Optional)이거나 `null` 값을 허용하는 필드는 Python의 타입 힌트와 기본값을 조합하여 매우 직관적으로 처리할 수 있습니다.

---

## 핵심 구문: `field: type | None = None`

```python
from pydantic import BaseModel

class Item(BaseModel):
    name: str  # 필수 필드
    description: str | None = None # 선택적/Nullable 필드
```

위 예제의 `description: str | None = None` 구문은 두 가지 중요한 역할을 합니다.

### 1. `str | None` (타입 힌트)

*   **의미:** "이 필드의 값은 `str` 타입이거나 `None` 타입일 수 있다"고 선언합니다.
*   **역할:** 클라이언트가 JSON 본문에 `"description": null`과 같이 명시적으로 `null`을 보내는 것을 허용합니다.
*   **참고:** Python 3.10 이전 버전에서는 `Optional[str]`와 동일합니다.

### 2. `= None` (기본값)

*   **의미:** "만약 클라이언트가 요청 시 이 필드를 아예 포함하지 않으면, 기본값으로 `None`을 사용한다"고 선언합니다.
*   **역할:** 필드 자체를 선택적으로 만듭니다. 이 필드가 없어도 유효성 검사 오류가 발생하지 않습니다.

## 동작 방식 요약

`description: str | None = None` 필드에 대한 클라이언트의 요청에 따라 값은 다음과 같이 결정됩니다.

| 클라이언트 요청 | 결과 (`item.description`) |
| :--- | :--- |
| `"description": "Some text"` | `"Some text"` (str) |
| `"description": null` | `None` |
| `description` 필드 없음 | `None` |

반면, `name: str`과 같이 기본값이 없는 필드는 요청 본문에 반드시 포함되어야 하며, 누락 시 Pydantic이 자동으로 `422 Unprocessable Entity` 유효성 검사 오류를 반환합니다.
