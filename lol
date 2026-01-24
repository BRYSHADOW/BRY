local player = game.Players.LocalPlayer
local char = player.Character or player.CharacterAdded:Wait()

local head = char:WaitForChild("Head")

-- Tăng kích thước đầu
head.Size = Vector3.new(25, 25, 25) -- chỉnh số này càng lớn càng to

-- Giữ đầu không bị văng
local weld = Instance.new("WeldConstraint")
weld.Part0 = head
weld.Part1 = char:WaitForChild("HumanoidRootPart")
weld.Parent = head

-- Tắt va chạm cho đỡ lag
head.CanCollide = false

-- Scale mặt cho đúng
for _, v in pairs(head:GetChildren()) do
	if v:IsA("Decal") then
		v.Face = Enum.NormalId.Front
	end
end
