class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ns, nt = len(s), len(t)
        if ns < nt:
            return ""

        ds, dt = {}, {}
        for i in range(nt):
            dt[t[i]] = 1 + dt.get(t[i], 0)
            ds[s[i]] = 1 + ds.get(s[i], 0)

        n = 0
        for key in dt:
            if dt[key] <= ds.get(key, 0):
                n += 1

        min_l, left = float("inf"), 0
        best_l, best_r = 0, 0

        for right in range(nt, ns):
            while n == len(dt):
                if min_l > right - left:
                    min_l = right - left
                    best_l = left
                    best_r = right
                if min_l == nt:
                    return s[left : right]

                ch_left = s[left]
                if ch_left in dt and ds[ch_left] == dt[ch_left]:
                    n -= 1
                ds[ch_left] -= 1
                if ds[ch_left] == 0:
                    del ds[ch_left]
                left += 1

            ch_right = s[right]
            ds[ch_right] = 1 + ds.get(ch_right, 0)
            if ch_right in dt and ds[ch_right] == dt[ch_right]:
                n += 1

        while n == len(dt):
            if min_l > ns - left:
                min_l = ns - left
                best_l = left
                best_r = ns
            if min_l == nt:
                return s[left : ns]

            ch_left = s[left]
            if ch_left in dt and ds[ch_left] == dt[ch_left]:
                n -= 1
            ds[ch_left] -= 1
            if ds[ch_left] == 0:
                del ds[ch_left]
            left += 1

        if min_l == float("inf"):
            return ""
        return s[best_l : best_r]