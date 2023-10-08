import os

def get_files_in_dir(dir_path):
  """Returns a list of all files in the given directory."""
  files = []
  print(dir_path)
  for root, dirs, filenames in os.walk(dir_path):
    print("root ", root, " dirs:", dirs, " filenames:", filenames)
    for filename in filenames:
      print(os.path.join(root, filename))
      files.append(os.path.join(root, filename))
  print("done get files")
  return files

def run_face_swapper(target_dir, source_dir, output_dir, execution_provider, frame_processor):
  """Runs the face swapper on all files in the target and source directories."""
  for target_file in get_files_in_dir(target_dir):
    for source_file in get_files_in_dir(source_dir):
      # Concatenate variables into a filename like {source}-{target}.mp4
      output_filename = os.path.join(output_dir, f"{os.path.basename(source_file)}-{os.path.basename(target_file)}")

      if os.path.exists(output_filename):
          print(f"Skipping as output file {output_filename} already exists.")
          continue

      # Run the face swapper
      print(f"python run.py --target {target_file} --source {source_file} -o {output_filename} --execution-provider {execution_provider} --frame-processor {frame_processor}")
      os.system(f"python run.py --target {target_file} --source {source_file} -o {output_filename} --execution-provider {execution_provider} --frame-processor {frame_processor}")

# Example usage:
print("Running faceswapper")
run_face_swapper("batch-mp4/", "batch-jpg/", "out/", "cuda", "face_swapper face_enhancer")

print("DONE!")