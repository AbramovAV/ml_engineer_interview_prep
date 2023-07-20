class Solution:
    from collections import deque
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        survived_asteroids = deque()
        for asteroid in asteroids:
            if len(survived_asteroids) == 0 or asteroid > 0:
                survived_asteroids.append(asteroid)
            elif asteroid < 0:
                while survived_asteroids:
                    if survived_asteroids[-1] < 0:
                        survived_asteroids.append(asteroid)
                        break
                    elif survived_asteroids[-1] < (asteroid * -1):
                        survived_asteroids.pop()
                    elif survived_asteroids[-1] == (asteroid * -1):
                        survived_asteroids.pop()
                        break
                    elif survived_asteroids[-1] > (asteroid * -1):
                        break
                else:
                    survived_asteroids.append(asteroid)
        return list(survived_asteroids)