# ⭐ Problem Explanation: Minimum Cost to Make Two Strings Identical

## 🔹 Problem Statement

Humein **do strings** s aur t diye gaye hain (same length).

Humein kuch **allowed character transformations** bhi diye gaye hain. Har transformation ka  **source character** ,  **target character** , aur **cost** di gayi hoti hai.

Aap  **s ya t dono me se kisi par bhi** , **kitni bhi baar** transformations apply kar sakte ho.

🎯 **Goal:**

Minimum total cost me s aur t ko **exactly same string** banana hai.

Agar possible nahi ho, to `-1` return karo.

---

# 📌 Example Breakdown

### **Example 1**

```
s = "abcc"
t = "bccc"
transform = (a→b cost 2), (b→c cost 1), (c→a cost 4)
```

* s[0] = 'a', t[0] = 'b' → ‘a’ → ‘b’ (cost 2)
* s[1] = ‘b’, t[1] = ‘c’ → ‘b’ → ‘c’ (cost 1)
* Baaki characters same hain.

✔ **Total Cost = 3**

---

### **Example 2**

```
s = "az"
t = "dc"
Possible path: a→b→c→d (cost 5 + 3 + 2 = 10)
z→c (cost 10)
```

✔ Total = 10 + 10 = **20**

---

### **Example 3**

```
s = "xyz"
t = "xzy"
Transform: x→y, x→z
```

* But s[1]=‘y’ ko t[1]=‘z’ banana ka koi path hi nahi.
* ❌ Not possible.

So answer = **-1**

---

# 🧠 Important Notes / Key Points

* Har character ko kisi **third character** me transform karna allowed hai.
* Hum **direct** transformation hi nahi, **indirect paths** bhi use kar sakte hain.

  Example: a→b→c→d allowed hai.
* Minimum cost find karne ke liye humein **all-pairs shortest path** chahiye.
* Characters fixed set:  **26 lowercase English letters** .

---

# 🔍 Approaches to Think About

## **Naive Approach (Wrong / Inefficient)**

* Har index par brute-force check karo ki s[i] → t[i] possible hai ya nahi.
* Indirect transformations ka path manually dhundhna impossible ho jayega.

❌ Works nahi karega.

---

## **Correct Strategy**

We need to know  **minimum cost to convert any character x into any character y** .

This is a classic  **graph problem** :

* Characters = nodes (26 nodes)
* Transformations = directed edges with weights = cost

We need  **shortest path between every pair of characters** .

✔ Best fit: **Floyd–Warshall Algorithm**

---

# 🏁 Floyd–Warshall Algorithm (Concept + Loop Intuition)

### 💡 Short Explanation

Floyd–Warshall ek algorithm hai jo **har node se har node tak** ka **minimum distance** find karta hai.

Graph size chhota hai (26×26), so perfect choice.

### 🔥 Core Idea

Har node `k` ko try karo as an intermediate.

Check:

```
distance[i][j]  
vs  
distance[i][k] + distance[k][j]
```

Agar intermediate se jaana cheap ho, update kar do.

### 🔁 Loop Order

```cpp
for k = 0 to 25:
    for i = 0 to 25:
        for j = 0 to 25:
```

* Outer loop `k`: intermediate node
* Middle loop `i`: start
* Inner loop `j`: end

---

# 🧩 Final Approach Summary

1. 26×26 cost matrix banao.
   * Pehle sabko `∞` rakho.
   * Diye gaye transformations fill karo.
   * Diagonal = 0.
2. **Floyd–Warshall** chalao taaki har pair ka minimum cost mil jaye.
3. Har index i ke liye:
   * s[i] = a
   * t[i] = b
   * Kisi **common character ch** pe dono ko convert karo →

     cost = cost[a→ch] + cost[b→ch]
4. Har index ka best cost sum karo.
5. Agar kisi index par possible nahi, return `-1`.

---

# 🧱 Code Explanation

### **1. Cost Matrix Initialization**

```cpp
vector<vector<int>> mincost(26, vector<int>(26, INT_MAX));
```

* 26×26 matrix, initially everything infinite.

```cpp
mincost[src][dst] = min(existing cost, given cost)
```

* Yeh direct edges set karta hai.

```cpp
for(i=0→25) mincost[i][i] = 0;
```

* Character to itself = free.

---

### **2. Floyd–Warshall**

```cpp
for k in 0..25:
  for i in 0..25:
    for j in 0..25:
        if path i→k and k→j valid:
            mincost[i][j] = min(mincost[i][j], i→k + k→j)
```

* Yahi step indirect transformations allow karta hai.

---

### **3. Per-Index Comparison**

Har index par:

* s[i] ko kis ch me convert ho sakta hai
* t[i] ko kis ch me convert ho sakta hai

Minimum choose karo:

```cpp
temp = min_over_all_ch ( mincost[a][ch] + mincost[b][ch] )
```

Agar temp still ∞:

→ No way to match these characters → return -1.

---

### **4. Sum All Costs**

`ans += temp`

Finally `ans` return.

---

# 📊 Complexity Analysis

### **Time**

* Floyd–Warshall: `26³ = ~17,576` operations

  → negligible.
* Processing string of length n: `26 * n`

**Total:** `O(26³ + 26n)` → practically **O(n)**

### **Space**

* Matrix: `26×26 = 676 integers`

Super efficient.

---

# ✅ Final Takeaways

* Problem graph + DP combination hai.
* Indirect transformations allow karne ke liye Floyd–Warshall perfect hai.
* Har index par best common character dhoondna optimal approach hai.
* Complete solution extremely optimal and scalable.
