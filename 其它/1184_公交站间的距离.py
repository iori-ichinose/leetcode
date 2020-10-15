class Solution:
    def distanceBetweenBusStops(self, distance: list, start: int, destination: int) -> int:
        # 方便计算，确保start < destination
        if start > destination:
            start, destination = destination, start
        elif start == destination:
            return 0

        # 计算直接从start到destination的距离
        to_dis = sum(distance(start, destination))
        # 另一个距离用一圈的距离减去上次求的距离
        out_dis = sum(distance) - to_dis

        return min(to_dis, out_dis)
