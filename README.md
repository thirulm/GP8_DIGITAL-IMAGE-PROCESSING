# GP8_DIGITAL-IMAGE-PROCESSING

Teamwork & Collaboration: Project Segmentation
Topic: Automated Object Segmentation and Background Removal
To achieve a professional workflow for our image processing project, we divided our responsibilities into Core Algorithmic Development and Refinement & Data Visualization:

Aliah Thaqifah (Technical Foundation & Threshold Optimization):
Core Logic Development: Authored the manual Otsu’s Thresholding script to mathematically calculate the optimal intensity value for separating the foreground object from the background.

Threshold Calibration: Conducted extensive testing to determine the Adjusted Threshold Offset (-35), ensuring that darker green sections and leaf veins were accurately preserved.

Binary-to-RGB Mapping: Developed the 3D-array expansion logic that allows the 2D binary mask to correctly isolate colors from the original RGB image.

Thiruvanandhan (Diagnostic Refinement & Visual Engineering):
Morphological Cleanup: Implemented Binary Opening operations to automatically erase noise and speckles from the background, ensuring a pure black result.

Structural Integrity: Applied Hole-Filling algorithms to ensure the segmented leaf appeared as a solid, continuous object without internal gaps or missing veins.

Visual Presentation: Engineered the 4-panel diagnostic layout, including personalized titling and automated coordinate offsets to ensure high readability for the final report.

Collaborative Effort: We worked together during the Edge Verification Phase to ensure the boundary between the "Object Only" and "Background Only" results was sharp and accurate across different leaf species, including Tomato, Ash Gourd, and Bitter Gourd.
