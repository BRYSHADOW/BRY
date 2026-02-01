local player = game.Players.LocalPlayer
local char = player.Character or player.CharacterAdded:Wait()

local head = char:WaitForChild("Head")
local humanoid = char:WaitForChild("Humanoid")

-- Size đầu (to nhưng không che)
local HEAD_SIZE = 25

head.Size = Vector3.new(HEAD_SIZE, HEAD_SIZE, HEAD_SIZE)
head.CanCollide = false

-- Xóa Motor cũ nối cổ
local neck = head:FindFirstChild("Neck")
if neck then
	neck:Destroy()
end

-- Tạo Weld mới và đẩy đầu lên cao
local weld = Instance.new("Weld")
weld.Part0 = char:WaitForChild("UpperTorso") or char:WaitForChild("Torso")
weld.Part1 = head

-- Đẩy đầu lên trên (số càng lớn càng cao)
weld.C0 = CFrame.new(0, 3 + (HEAD_SIZE / 2), 0)

weld.Parent = head
