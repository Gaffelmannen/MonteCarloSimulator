#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import matplotlib.pyplot as plt

from datetime import date

class MonteCarloSimulator:

    def __init__(self):
        self.num_samples = 1000
        self.pi_estimate = None
        self.x_vals = None
        self.y_vals = None

    def _write_to_file(self, text_to_write):
        f = open(f"mote_carlo_{date.today()}.txt", "a")
        f.write(text_to_write)
        f.close()

    def _monte_carlo_pi(self):
        inside_circle = 0
        points_x, points_y = [], []
        
        for _ in range(self.num_samples):
            x, y = random.uniform(-1, 1), random.uniform(-1, 1)
            points_x.append(x)
            points_y.append(y)
            
            if x**2 + y**2 <= 1:
                inside_circle += 1
        
        pi_estimate = (inside_circle / self.num_samples) * 4

        return pi_estimate, points_x, points_y

    def run_simulation(self):
        self.pi_estimate, self.x_vals, self.y_vals = self._monte_carlo_pi()
        self._plot_it()
        self._write_to_file(f"Samples: {self.num_samples}\t\tEstimated π: {self.pi_estimate}\n")
        print(f"After {self.num_samples} samples - Estimated π: {self.pi_estimate}")

    def _plot_it(self):
        fig, ax = plt.subplots()
        circle = plt.Circle((0, 0), 1, color='r', fill=False)
        ax.add_patch(circle)
        ax.set_xlim(-1, 1)
        ax.set_ylim(-1, 1)
        ax.set_aspect('equal')
        ax.scatter(self.x_vals, self.y_vals, s=1)
        ax.set_title(f"Monte Carlo π Estimate: {self.pi_estimate:.5f} with {self.num_samples} samples")
        plt.savefig("img/mote_carlo_pi_{}.png".format(self.num_samples), bbox_inches="tight")

if __name__ == "__main__":
    mcs = MonteCarloSimulator()
    for _ in range(0, 100):
        mcs.run_simulation()
        mcs.num_samples += 1000
