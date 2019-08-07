# Two Sum II - Input array is sorted

[leetcode](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) (2019.08.07)

![image](https://user-images.githubusercontent.com/40231980/62590565-c73bb780-b907-11e9-88e0-6d087ecc0dbd.png)

### # 문제

오름차순으로 정렬된 `numbers`에서 두 수를 합하여 target이 되는 index 리스트 반환.  
단, 동일 요소 두 번 사용 불가.

### # 해결

정렬되어 있는 리스트이기 때문에 앞/뒤로 포인터를 이동해가면서 해결하면 된다.

- start(앞) 와 end(뒤) 라고 포인터를 지정했고,
  - `start + end == target`인 경우 `종료`
  - `start + end < target` 인 경우 값을 `증가`시키기 위해 `START = START + 1`
  - `start + end > target` 인 경우 값을 `감소`시키기 위해 `END = END - 1`

![image](https://user-images.githubusercontent.com/40231980/62590586-d589d380-b907-11e9-8e59-861731f132db.png)
