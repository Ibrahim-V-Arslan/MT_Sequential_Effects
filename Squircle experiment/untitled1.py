# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 15:36:45 2023

@author: veoni
"""

c1 = visual.Circle(win, units = "pix", size = (70), pos = positions[0], colorSpace = "rgb255", lineColor = training_df['RGB_1'].iloc[0], fillColor = training_df['RGB_1'].iloc[0])
c2 = visual.Circle(win, units = "pix", size = (70), colorSpace = "rgb255", lineColor = ((m_range[0][1]*255), 0, ((1-m_range[0][1])*255)),pos = (125,395), fillColor = ((m_range[0][1]*255), 0, ((1-m_range[0][1])*255)))
c3 = visual.Circle(win, units = "pix", size = (70), colorSpace = "rgb255", lineColor = ((m_range[0][2]*255), 0, ((1-m_range[0][2])*255)),pos = (175,270), fillColor = ((m_range[0][2]*255), 0, ((1-m_range[0][2])*255)))
c4 = visual.Circle(win, units = "pix", size = (70), colorSpace = "rgb255", lineColor = ((m_range[0][3]*255), 0, ((1-m_range[0][3])*255)),pos = (125,145), fillColor = ((m_range[0][3]*255), 0, ((1-m_range[0][3])*255)))
c5 = visual.Circle(win, units = "pix", size = (70), colorSpace = "rgb255", lineColor = ((m_range[0][4]*255), 0, ((1-m_range[0][4])*255)),pos = (0,95), fillColor = ((m_range[0][4]*255), 0, ((1-m_range[0][4])*255)))
c6 = visual.Circle(win, units = "pix", size = (70), colorSpace = "rgb255", lineColor = ((m_range[0][5]*255), 0, ((1-m_range[0][5])*255)) ,pos = (-125,145), fillColor = ((m_range[0][5]*255), 0, ((1-m_range[0][5])*255)))
c7 = visual.Circle(win, units = "pix", size = (70), colorSpace = "rgb255", lineColor = ((m_range[0][6]*255), 0, ((1-m_range[0][6])*255)),pos = (-175,270), fillColor = ((m_range[0][6]*255), 0, ((1-m_range[0][6])*255)))
c8 = visual.Circle(win, units = "pix", size = (70), colorSpace = "rgb255", lineColor = ((m_range[0][7]*255), 0, ((1-m_range[0][7])*255)),pos = (-125,395), fillColor = ((m_range[0][7]*255), 0, ((1-m_range[0][7])*255)))
