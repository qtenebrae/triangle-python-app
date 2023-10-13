# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres
to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.0.1] - 2023-10-13

### Added

- Module `App`, to create an application with a moving ball in a triangular area.
- `App start`, to start the ball rolling on the canvas.
- `App stop`, to reset the variable values to the original values.
- `App validate`, to check the validity of the entered data in the widget.
- `App save_old_value`, to save the previous widget value.
- `App modal_help`, to display a modal window with help text.
- `App modal_about`, to display the "About" modal window.
- Module `MovingBall`, representing a moving ball on a canvas.
- `MovingBall distance_to_segment`, to calculates the distance from a ball to an edge on the canvas.
- `MovingBall move_ball`, to move the ball across the canvas and reflect it off the walls if it collides with them.
- `MovingBall clear_ball`, to remove the balloon and all other objects on the canvas.
- Module `Validator`, to verify the data entered.
- `Validator validate_int`, to check if the value is an integer.
- Module `Controller`.
- `Controller get_version`, to return the system version.
- `Controller get_help`, for the return of the programme certificate.
- Module `Storage`, representing a repository.
- `Storage read_version`, to read a version from a file.
- `Storage read_help`, to read help from the file.