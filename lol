local player = game.Players.LocalPlayer
local char = player.Character or player.CharacterAdded:Wait()

-- ====== CHỈNH SIZE Ở ĐÂY ======
local HEAD_SIZE = Vector3.new(0.1,0.1,0.1)
local TORSO_SCALE = 0.1
local LIMB_SCALE = 0.1
-- ==============================

-- HÀM SCALE PART
local function scalePart(part, scale)
	if part and part:IsA("BasePart") then
		part.Size = part.Size * scale
		part.CanCollide = false
	end
end

-- ====== ĐẦU ======
local head = char:FindFirstChild("Head")
if head then
	head.Size = HEAD_SIZE
	head.CanCollide = false

	-- Xóa cổ cũ
	local neck = head:FindFirstChild("Neck")
	if neck then neck:Destroy() end

	-- Gắn lại đầu cho không che thân
	local torso = char:FindFirstChild("UpperTorso") or char:FindFirstChild("Torso")
	if torso then
		local weld = Instance.new("Weld")
		weld.Part0 = torso
		weld.Part1 = head
		weld.C0 = CFrame.new(0, 3 + (HEAD_SIZE.Y / 2), 0)
		weld.Parent = head
	end
end

-- ====== THÂN ======
scalePart(char:FindFirstChild("UpperTorso"), TORSO_SCALE)
scalePart(char:FindFirstChild("LowerTorso"), TORSO_SCALE)
scalePart(char:FindFirstChild("Torso"), TORSO_SCALE) -- R6

-- ====== TAY ======
scalePart(char:FindFirstChild("LeftUpperArm"), LIMB_SCALE)
scalePart(char:FindFirstChild("LeftLowerArm"), LIMB_SCALE)
scalePart(char:FindFirstChild("LeftHand"), LIMB_SCALE)

scalePart(char:FindFirstChild("RightUpperArm"), LIMB_SCALE)
scalePart(char:FindFirstChild("RightLowerArm"), LIMB_SCALE)
scalePart(char:FindFirstChild("RightHand"), LIMB_SCALE)

-- ====== CHÂN ======
scalePart(char:FindFirstChild("LeftUpperLeg"), LIMB_SCALE)
scalePart(char:FindFirstChild("LeftLowerLeg"), LIMB_SCALE)
scalePart(char:FindFirstChild("LeftFoot"), LIMB_SCALE)

scalePart(char:FindFirstChild("RightUpperLeg"), LIMB_SCALE)
scalePart(char:FindFirstChild("RightLowerLeg"), LIMB_SCALE)
scalePart(char:FindFirstChild("RightFoot"), LIMB_SCALE)

print("DONE: Đã scale từng phần nhân vật")
