import java.util.Arrays;
import java.util.Comparator;

public class Solution {
    class Event {
        int time;
        boolean isStart;

        Event(int time, boolean isStart) {
            this.time = time;
            this.isStart = isStart;
        }
    }

    public int solution(int[][] lines) {
        Event[] events = new Event[lines.length * 2];
        int idx = 0;
        for (int[] line : lines) {
            events[idx++] = new Event(line[0], true);
            events[idx++] = new Event(line[1], false);
        }

        Arrays.sort(events, Comparator.comparingInt(e -> e.time));

        int currentOverlap = 0, lastTime = 0;
        int totalOverlap = 0;
        for (Event event : events) {
            if (currentOverlap >= 2) {
                totalOverlap += event.time - lastTime;
            }
            if (event.isStart) {
                currentOverlap++;
            } else {
                currentOverlap--;
            }
            lastTime = event.time;
        }

        return totalOverlap;
    }
}