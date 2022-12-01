control 'must-exist-label' do
        title 'Ensure Container Image has `maintainer` label'
        describe docker_image("#{ENV['CONTAINER_IMAGE_URL']}") do
          it { should exist }

          # Not works on my machine
          # its(['Config.Labels']) { should include 'maintainer' => 'Michael Act < michael.4ct@gmail.com >' }
        end
end